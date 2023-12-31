from sqlalchemy import Table, Column, Integer, TIMESTAMP, String, MetaData

metadata = MetaData()

operations = Table(
    'operations',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('quantity', String),
    Column('figi', String),
    Column('instrument_type', String, nullable=True),
    Column('date', TIMESTAMP),
    Column('type', String),
)
