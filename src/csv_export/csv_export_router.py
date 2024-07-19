from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_async_session
from csv_export.csv_export_service import ExportService
from model import student_model, class_model, teacher_class_model, inscription_model, pack_model, level_model,teacher_model

# Create a new FastAPI router
router = APIRouter(prefix="/csv", tags=["csv"])

# Create a new instance of the ExportService class
export_service = ExportService()

# Map table names to their respective model classes
table_models_map = {'student' : student_model.StudentModel,
                    'class' : class_model.ClassModel,
                    'inscription' : inscription_model.InscriptionModel,
                    'level' : level_model.LevelModel,
                    'pack' : pack_model.PackModel,
                    # 'pagos' : paymentModel.Payment_model,
                    'teacher' : teacher_model.TeacherModel,
                    'teacher_class' : teacher_class_model.TeacherClassModel}

# Define a route to export a table to a CSV file
@router.get("/{table_name}")
async def export_csv(table_name: str, db: AsyncSession = Depends(get_async_session)):
    return await export_service.export_csv(db, table_models_map[table_name], f"{table_name}.csv")

