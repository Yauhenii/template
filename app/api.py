from fastapi import FastAPI
from stub import create_entity_by_index

from model import Entity

app = FastAPI()


@app.get("/entity/get/by-index/{index}", response_model=Entity)
async def get_entity_by_index(index):
    return create_entity_by_index(int(index))
