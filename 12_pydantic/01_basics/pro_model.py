from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price:float
    in_stock: bool = True



product_one = Product(id=1, name="Laptop", price=333.33,in_stock=True)
product_Two = Product(id=2, name="mouse", price=333.33)
product_three = Product(id=2, name="keyboard")
