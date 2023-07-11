from fastapi import FastAPI
from ecommerce import Customer

app = FastAPI()
customers = Customer.load_customers_from_json("data/customers.json")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/customers")
async def get_customers():
    return customers

@app.get("/customers/{customer_id}")
async def get_customer(customer_id: int):
    return customers[customer_id -1]
