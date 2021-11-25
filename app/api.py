from fastapi import FastAPI

from stub import create_entity_by_index, create_entity
from model import Entity

app = FastAPI()


@app.get("/entity/get/by-index/{index}", response_model=Entity)
async def get_entity_by_index(index) -> Entity:
    return create_entity_by_index(index)


@app.post("/entity/post/name={name}&index={index}&number={number}&date={date}")
async def post_entity_by_index(name, index, number, date) -> Entity:
    return create_entity(name, index, number, date)
