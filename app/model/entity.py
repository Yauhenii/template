from pydantic.main import BaseModel
from datetime import date


class Entity(BaseModel):
    entity_name: str
    entity_index: int
    entity_number: float
    entity_date: date