import time

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operations

from operations.schemas import OperationCreate

router = APIRouter(
    prefix='/operations',
    tags=['Operations']
)


@router.get('/long_operation')
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return 'Too many long operations'


@router.get('/')
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operations).where(operations.c.type == operation_type)
    print(query)
    result = await session.execute(query)
    return result.all()


@router.post('/')
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operations).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}

