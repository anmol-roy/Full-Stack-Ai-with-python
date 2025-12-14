# from pydantic import BaseModel, computed_field,Field_validator, Field

# class Product(BaseModel):
#     price: float
#     quantity: int

#     @computed_field
#     @property

#     def total_cost(self) -> float:
#         return self.price * self.quantity
    

# classs Booking(BaseModel):

#     user_id: int
#     room_id: int
#     nights: int = Field(..., ge=1)
#     rate_per_night: float = Field(..., gt=0)

# D:\d\Genai\00_python
#     @computed_field
#     @property
#     def total_price(self) -> float:
#         return self.nights * self.rate_per_night


    
