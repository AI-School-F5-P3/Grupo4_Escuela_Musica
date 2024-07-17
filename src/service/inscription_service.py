from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from model.student_model import StudentModel
from model.inscription_model import InscriptionModel
from scheme.inscription_scheme import Inscription
from dateutil.relativedelta import relativedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, text
from service.teacher_class_service import TeacherClassService
from logger import Logs
from sqlalchemy.future import select
from sqlalchemy import delete, func
from collections import defaultdict


class InscriptionService:
    def __init__(self):
        self.logger = Logs()
    

    async def consult_inscriptions(self, db: AsyncSession):
        async with db.begin():
            result = (await db.execute(select(InscriptionModel))).scalars().all()
        self.logger.debug('Consult all inscriptions')
        if not result:
            self.logger.warning("Inscriptions not found")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "No insctiptions exists")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))



    async def consult_inscription_id(self, id: int, db: AsyncSession):
        async with db.begin():
            result = (await db.execute(select(InscriptionModel).filter(InscriptionModel.id_inscription == id))).scalars().all()
        self.logger.debug(f'Consult inscription by id: {id}')
        if not result:
            self.logger.warning(f"Inscription with the id - {id}  not found")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Inscription with the id - {id}  not found")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
   
    
    async def consult_paid_inscription(self, id:int, bolean: bool, db: AsyncSession):
        async with db.begin():
            result = (await db.execute(select(InscriptionModel).filter(InscriptionModel.id_student == id, InscriptionModel.paid == bolean)))
            rows = result.scalars().all()
        self.logger.debug(f'Consult paid inscription by student id: {id}')
        if not rows:
            self.logger.warning(f"Paid inscription with the id - {id}  not found")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "paid Inscription does not exist")
        return JSONResponse(status_code=200, content=jsonable_encoder(rows))
    


    # Create how many times a student is registered in the same pack
    async def repetition_pack(self, id_student: int, id_class_teacher: int, db: AsyncSession):
        
        TeacherClassService().consult_teacher_class_id(id_class_teacher, db)  # Ensure this coroutine is awaited
        
        query = text("""SELECT COUNT(name_pack) AS repetition
                        FROM inscription AS i
                        JOIN teacher_class AS tc ON tc.id_class_teacher = i.id_class_teacher
                        JOIN class AS c ON c.id_class = tc.id_class
                        JOIN pack AS p ON p.id_pack = c.id_pack
                        WHERE i.id_student = :id_student AND name_pack IN
                        (
                            SELECT name_pack
                            FROM teacher_class
                            JOIN class ON class.id_class = teacher_class.id_class
                            JOIN pack ON pack.id_pack = class.id_pack
                            WHERE teacher_class.id_class_teacher = :id_class_teacher
                        )
                        GROUP BY name_pack""")
    
        result = await db.execute(query, {"id_student": id_student, "id_class_teacher": id_class_teacher})
        rows = result.first()

        return [{'repetition': rows[0] if rows else 0}]
    
    #Consult the information of the pack to which the student wants to register
    async def data_pack(self, id: int, db: AsyncSession):
        query = text("""SELECT p.id_pack, p.name_pack, p.price_pack, p.first_discount, p.second_discount
                        FROM teacher_class AS tc
                        JOIN class AS c ON c.id_class = tc.id_class
                        JOIN pack AS p ON p.id_pack = c.id_pack
                        WHERE tc.id_class_teacher = :id""")

        result = await db.execute(query, {'id': id})
        rows = result.fetchall()
    
        if rows:
            self.logger.debug('Consulting the pack')
            result = [{"id_pack": data[0], "name_pack": data[1], "price_pack": data[2], "first_discount": data[3], "second_discount": data[4]} for data in rows]
        else:
            result = []
        return result

        
        
        
    # Create a new inscription
    async def create_new_inscription(self, data: Inscription, db: AsyncSession):
        async with db.begin():
            result = await db.execute(select(StudentModel).filter(StudentModel.id_student == data.id_student))
            student = result.scalars().first()
            if not student:
                self.logger.warning('student was not found')
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "student with this id doesn't exist")
            repetition_pack = await self.repetition_pack(data.id_student, data.id_class_teacher, db)
            data_pack = await self.data_pack(data.id_class_teacher, db)
            
            num_times_inscription = repetition_pack[0]["repetition"]
            first_discount = data_pack[0]['first_discount']
            second_discount = data_pack[0]["second_discount"]
            price_pack = data_pack[0]["price_pack"]
            family_discount = student.family_discount
            inscription_date = data.inscription_date
            
            # price_with_discount = 0.0  # Initialize the variable to ensure it is assigned
            

            if num_times_inscription == 0:
                price_with_discount = price_pack * (1 - family_discount)
                applied_discount = 0.0
            elif num_times_inscription == 1:
                price = price_pack * (1 - first_discount)
                price_with_discount = price * (1 - family_discount)
                applied_discount = first_discount
            else:
                price = price_pack * (1 - second_discount)
                price_with_discount = price * (1 -  family_discount)
                applied_discount = second_discount



            # Create a new instance of the Inscripcion model with the data provided
            new_inscription = InscriptionModel(
                id_class_teacher=data.id_class_teacher,
                id_student=data.id_student,
                price_class=price_pack,
                discount_inscription=applied_discount,
                family_discount=family_discount,
                price_with_discount = price_with_discount,
                paid=False,
                inscription_date=inscription_date,  # Fecha actual
                end_date= inscription_date + relativedelta(months=1)
                # With relativedelta(months=1) I add 1 month automatically
            )
            db.add(new_inscription)
            await db.commit()  # Commit changes to the database
            self.logger.info("The new registration has been registered")
            await db.close()
            return JSONResponse(status_code=201, content={"message": "A new registration has been registered"})

    # EDIT A REGISTRATION
    async def edit_inscription(self, id: int, data: Inscription, db: AsyncSession):
        async with db.begin():
            inscription = (await db.execute(select(InscriptionModel).filter(InscriptionModel.id_inscription == id))).scalars().first()
            if not inscription:
                self.logger.warning('Registration not found to edit')
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="inscription not found")

           
            inscription.paid = data.paid
            inscription.inscription_date = data.inscription_date

            await db.commit()
            self.logger.info("Registration has been modified")
            return JSONResponse(status_code=200, content={"message": "Registration has been modified"})


    # DELETE A REGISTRATION
    async def delete_inscription(self, id: int, db: AsyncSession):
        async with db.begin():
            inscription = (await db.execute(select(InscriptionModel).filter(InscriptionModel.id_inscription == id))).scalars().first()
            if not inscription:
                self.logger.warning('The student to delete was not found')
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registration not found")

            await db.execute(delete(InscriptionModel).filter(InscriptionModel.id_inscription == id))
            await db.commit()
            self.logger.info('Registration has been removed')
            return JSONResponse(status_code=200, content={"message": "Registration has been removed"})
        

     # SEGREGRAR INSCRIPCIONES POR MES
    async def inscriptions_by_month(self, db: AsyncSession):
        result = (await db.execute(select(InscriptionModel,func.date_trunc('month', InscriptionModel.inscription_date).label('month')))).all()
        self.logger.debug('Consult inscriptions by months')
        if not result:
            self.logger.warning('There is no inscription')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There is no inscription')

        inscriptions_by_month = defaultdict(list) # group inscriptions by month
        for inscription, month in result:
        # Format the month as "Month Year"
            formatted_month = month.strftime("%B %Y")
            inscriptions_by_month[formatted_month].append(inscription)  # append inscriptions to the corresponding month

        self.logger.info('Consult inscriptions by months')
        return JSONResponse(status_code=200, content=jsonable_encoder(inscriptions_by_month))

        
        
        


