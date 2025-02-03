from enum import Enum
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def root():
    return {"message": "hello world"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}



@app.put("/")
async def put():

        return {"messsage": " Put , rotası"}

@app.get("/users")
async def list_items():
    return {"message":"List items route"}

@app.get("/users/me")
async def get_current_user():
    return {"Message":" this is the current user"}


@app.get("/users/{user_id}")
async def get_item(user_id: str):
    return {"user_id": user_id}

class FoodEnum(str, Enum):
    fruits = "furits"
    vegatables = "vegatables"
    dairy= "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegatables:
        return {"foodname": food_name , "Messsage ": "you are healthy"}

    if food_name.value == 'furits':
        return {"foodname": food_name , "Messsage ": "you are still healthy, but like sweet things"}

    return {"foodname": food_name , "Messsage ": "çikolatalı süt içerim"}


fake_items_db = [{"items_name": "Foo"},{"items_name": "Bass"},{"items_name": "Bazz"}]

@app.get("/items")
async def list_items(skip: int = 0 , limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, sample_query_param: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id , "sample_query_param": sample_query_param} 
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description": "Deneme açıklama lorem ipsum"})
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool= False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description": "Deneme açıklama lorem ipsum"})
    return item