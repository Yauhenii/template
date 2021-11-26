from fastapi import FastAPI
import logging

from stub import create_entity_by_index, create_entity
from model import Entity

app = FastAPI()
logger = logging.getLogger('uvicorn.error')


@app.get("/entity/get/by-index/{index}", response_model=Entity)
async def get_entity_by_index(index) -> Entity:
    entity = create_entity_by_index(index)
    logger.info(entity)
    return entity


@app.post("/entity/post/name={name}&index={index}&number={number}&date={date}")
async def post_entity_by_index(name, index, number, date) -> Entity:
    entity =  create_entity(name, index, number, date)
    logger.info(entity)
    return entity
