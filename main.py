from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#Create a Pydantic model which allows more complex data structures to be passed into the server
class Item(BaseModel):
    #Not providing a default causes the text field to become a requirement
    text: str
    is_done: bool = False

#Basic list of items that was used at the start of the example
items = []

@app.get("/")
def root():
    return {"Hello": "World"}

#Add a new item to the list
@app.post("/items")
def create_items(item: Item):
    items.append(item)
    return items

#Get the number of items from the list. Use a default value of 10, however accept a int value provided for the user aswell
@app.get("/items")
def list_items(limit: int = 10, response_model=list[Item]):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} Not Found")
