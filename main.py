from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a simple route (endpoint)
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

#path parameters
#basics
@app.get("/items/{item_id}/")
def read_items(item_id:int):
    return {"item_id":item_id}

#multipath parameters


@app.get("/items/{item_id}/orders/{order_id}/")
def read_items(item_id:int,order_id:int):
    return {"item_id":item_id,"order_id":order_id}