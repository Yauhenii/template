from fastapi import FastAPI
from datetime import date

from model import Entity

app = FastAPI()


@app.get("/entity/get/by-index/{index}", response_model=Entity)
async def get_entity_by_index(index):
    entity = Entity(
        entity_name="entity" + index,
        entity_index=int(index),
        entity_number=float(index)/0.999,
        entity_date=date.today(),
    )
    return entity
