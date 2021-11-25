from datetime import date

from model import Entity


def create_entity_by_index(index: int) -> Entity:
    entity = Entity(
        entity_name="entity" + str(index),
        entity_index=index,
        entity_number=float(index) / 0.999,
        entity_date=date.today(),
    )
    return entity
