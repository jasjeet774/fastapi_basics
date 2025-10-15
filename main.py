from fastapi import FastAPI

from fastapi import Query
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

# Path parameters with string types and slug usage
# Slugs often include - and letters. No int conversion needed.

@app.get("/posts/{slug}/")
def read_post(slug:str):
    return{"slug":slug}

#query parameters

@app.get("/search")
def search(q:str|None=None):
    return {"query":q}


# Query(...) marks it required (... is Ellipsis).
@app.get("/search")
def search(q: str = Query(...)):  # required
    return {"query": q}

# Path + query together

@app.get("/product/{product_id}")
def get_products(product_id:int,details:bool=False):
    return {"product_id":product_id,"details":details}

