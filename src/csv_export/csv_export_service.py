import csv
from io import StringIO # component for efficiently handling in-memory text data, particularly useful in web applications like FastAPI for generating and serving CSV data on-the-fly without the need for temporary files
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from logger import Logs
from fastapi import HTTPException, status
from fastapi.responses import StreamingResponse # StreamingResponse is a FastAPI response class that allows you to return large files in chunks, which is useful for streaming data to the client

logger = Logs()

class ExportService:
    def __init__(self):
        self.logger = logger

    async def export_csv(self,db: AsyncSession, model: object, filename: str):
        async with db.begin():
            result = (await db.execute(select(model))).scalars().all()
        if not result:
            self.logger.warning('No records found')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message":"No records found"})


        # get the column names from the model
        column_names = [column.name for column in model.__table__.columns]

        # Create a StringIO object to write the CSV data to
        output = StringIO()
        # Create a CSV writer object
        writer = csv.writer(output)
        # Write the header row
        writer.writerow(column_names)
        # Write the data rows
        for row in result:
            writer.writerow([getattr(row, column) for column in column_names])

        output.seek(0)  # Move the cursor to the start of the StringIO object
        # Return the CSV data and set the content type to text/csv so the browser knows to download it as a file
        return StreamingResponse(content=output, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename={filename}"})
