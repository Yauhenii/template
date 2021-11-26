from datetime import date

from pydantic.main import BaseModel


class Entity(BaseModel):
    entity_name: str
    entity_index: int
    entity_number: float
    entity_date: date
