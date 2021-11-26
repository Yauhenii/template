from datetime import date as dt

from app.model import Entity


def create_entity(name: str, index: int, number: float, date: dt) -> Entity:
    entity = Entity(
        entity_name=name,
        entity_index=index,
        entity_number=number,
        entity_date=date,
    )
    return entity


def create_entity_by_index(index: int) -> Entity:
    entity = Entity(
        entity_name="entity" + str(index),
        entity_index=index,
        entity_number=float(index) / 0.999,
        entity_date=dt.today(),
    )
    return entity
