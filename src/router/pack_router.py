from fastapi import APIRouter, Depends  # Import APIRouter and Depends from FastAPI for routing and dependency injection
from scheme.pack_scheme import Pack  # Import the Pack schema
from service.pack_service import PackService  # Import the PackService class
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for asynchronous database operations
from config.db import get_async_session  # Import the function to get an async session

# Create an APIRouter instance with a prefix and tags for routes related to pack
router = APIRouter(prefix="/pack", tags=["pack"])
# Instantiate the PackService class
pack_service = PackService()

# Consult all packs
@router.get('/')
# Define an async function to consult all packs, with dependency injection for the database session
async def consult_packs(db: AsyncSession = Depends(get_async_session)):
    return await pack_service.consult_packs(db)  # Call the consult_packs method from pack_service

# Consult a pack by id
@router.get('/{id}')  # 'id' is the path parameter when the user accesses this URL
# Define an async function to consult a pack by id, with dependency injection for the database session
async def consult_pack_id(id: int, db: AsyncSession = Depends(get_async_session)):
    return await pack_service.consult_pack_id(db, id)  # Call the consult_pack_id method from pack_service

# Add a new pack
@router.post('/')
# Define an async function to add a new pack, with dependency injection for the database session
async def add_pack(data: Pack, db: AsyncSession = Depends(get_async_session)):
    return await pack_service.add_pack(data, db)  # Call the add_pack method from pack_service

# Edit a pack's details
@router.put('/{id}')
# Define an async function to edit a pack's details, with dependency injection for the database session
async def edit_pack(id: int, data: Pack, db: AsyncSession = Depends(get_async_session)):
    return await pack_service.edit_pack(id, data, db)  # Call the edit_pack method from pack_service

# Delete a pack
@router.delete('/{id}')
# Define an async function to delete a pack, with dependency injection for the database session
async def delete_pack(id: int, db: AsyncSession = Depends(get_async_session)):
    return await pack_service.delete_pack(id, db)  # Call the delete_pack method from pack_service
