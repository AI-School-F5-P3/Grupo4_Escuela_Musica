from fastapi.encoders import jsonable_encoder  # Import jsonable_encoder to convert data to JSON format
from fastapi.responses import JSONResponse  # Import JSONResponse to send JSON responses
from sqlalchemy import and_, text  # Import and_ and text for SQL operations
from model.payment_model import PaymentModel  # Import PaymentModel from the model
from scheme.payment_scheme import Payment  # Import Payment schema for data validation and serialization
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for asynchronous database sessions
from fastapi import HTTPException, status  # Import HTTPException and status for error handling
from model.inscription_model import InscriptionModel  # Import InscriptionModel from the model
from sqlalchemy.future import select  # Import select for SQL queries
from sqlalchemy import delete  # Import delete for SQL delete operations
from logger import Logs  # Import Logs for logging

class PaymentService:
    def __init__(self):
        self.logger = Logs()  # Initialize logger

    # Fetch all payments
    async def consult_payment_s(self, db: AsyncSession):
        async with db.begin():  # Start a database session
            result = (await db.execute(select(PaymentModel))).scalars().all()  # Execute a query to fetch all payments
        self.logger.debug('Fetching all payments')  # Log the action
        if not result:
            self.logger.warning('No payments found')  # Log a warning if no payments are found
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No payments found")  # Raise an HTTP 404 error if no payments
        return JSONResponse(status_code=200, content=jsonable_encoder(result))  # Return the result as a JSON response

    # Fetch a payment by student ID
    async def consultar_pago_por_id_del_alumno(self, id):
        query = f"""SELECT p.*, i.precio_con_descuento AS monto
                    FROM pagos AS p
                    JOIN inscripciones AS i ON i.id_inscripcion = p.inscripcion_id
                    WHERE i.alumno_id = {id}"""  # Define the query to fetch payment by student ID
        results = self.db.execute(text(query)).fetchall()  # Execute the query and fetch all results
        self.logger.debug(f'Fetching payment by student ID')  # Log the action

        if not results:
            self.logger.warning('Payment not found')  # Log a warning if no payment is found
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")  # Raise an HTTP 404 error if no payment

        result_dict = [{"id": item[0], "id_inscripcion": item[1], "fecha": item[2], "monto": item[3]} for item in results]  # Create a dictionary from the results
        return JSONResponse(status_code=200, content=jsonable_encoder(result_dict))  # Return the result as a JSON response

    # Add a new payment
    async def agregar_pago(self, data):
        pago = self.db.query(InscriptionModel)\
                      .filter(and_(InscriptionModel.id_inscripcion == data.inscripcion_id, InscriptionModel.pagada == 'false')).first()  # Query to check if the payment exists and is not paid
        if pago is None:
            self.logger.warning('Payment already exists with this ID')  # Log a warning if payment already exists
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment does not exist")  # Raise an HTTP 404 error if payment does not exist

        self.agregar_pago_en_inscripcion(data.inscripcion_id)  # Update the inscription with the new payment
        nuevo_pago = PaymentModel(**data.dict())  # Create a new PaymentModel instance
        self.db.add(nuevo_pago)  # Add the new payment to the database
        self.db.commit()  # Commit the transaction
        self.logger.info("A new payment has been registered")  # Log the action
        return JSONResponse(status_code=201, content={"message": "A new payment has been successfully registered"})  # Return a success message

    # Update the 'paid' status in the inscriptions table
    async def agregar_pago_en_inscripcion(self, id):
        inscripcion = self.db.query(InscriptionModel).filter(InscriptionModel.id_inscripcion == id).first()  # Query to find the inscription by ID
        inscripcion.pagada = 'true'  # Update the 'paid' status
        self.db.commit()  # Commit the transaction
        self.logger.info("A new payment has been added to the inscription")  # Log the action
        return JSONResponse(status_code=201, content={"message": "Payment has been added to the inscriptions table"})  # Return a success message
