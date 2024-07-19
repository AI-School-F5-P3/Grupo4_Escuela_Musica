from typing import List  # Importing List from typing for type hinting
from fastapi import APIRouter  # Importing APIRouter to create route endpoints
from fastapi.encoders import jsonable_encoder  # Importing jsonable_encoder to convert data to JSON format
from fastapi.responses import JSONResponse  # Importing JSONResponse to send JSON responses
from sqlalchemy.exc import SQLAlchemyError  # Importing SQLAlchemyError to handle database exceptions
from service.payment_service import PaymentService  # Importing the Pagos_services class for payment-related operations
from scheme.payment_scheme import Payment  # Importing the Pagos schema for data validation and serialization
from config.db import Base, engine  # Importing Base and engine to interact with the database


# Create an APIRouter instance for managing payment routes
Payment = APIRouter(tags=["payments"])

# CREATE PAYMENTS TABLE
# Uncomment the following lines if you need to create the database tables on startup

# @pagos.on_event("startup")
# def startup():
#      # Create database tables
#     Base.metadata.create_all(bind=engine)


# FETCH ALL PAYMENTS
@payment.get('/payments', response_model=list)  # Define a GET endpoint to fetch all payments, expecting a list response
def consult_payment():
    result = PaymentService().consult_payment_s()  # Call the service method to fetch all payments
    return result  # Return the result as a response


# FETCH PAYMENTS BY STUDENT ID
@payment.get("/payments/{id}", response_model=dict)  # Define a GET endpoint to fetch payments by student ID, expecting a dictionary response
def consult_payment_student_id(id_alumno: int):  # The endpoint receives a student ID as a path parameter
    result = PaymentService().consult_payment_with_student_ido(student_id)  # Call the service method to fetch payments by student ID
    return result  # Return the result as a response


# ADD A PAYMENT
@payment.post("/payments", response_model=dict)  # Define a POST endpoint to add a new payment, expecting a dictionary response
def add_payment(data: Payment) -> dict:  # The endpoint receives a payment data object in the request body
    result = PaymentService().add_payments(data)  # Call the service method to add the new payment
    return result  # Return the result as a response
