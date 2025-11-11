def chai_customer():
    print("welcome ! what chai would you like ?")
    order = yield
    while True:
        print(f"preparing your {order} chai")
        print("here is your chai")
        order = yield "chai served"

stall = chai_customer()
next(stall)  # Prime the generator


stall.send("masala")
print(stall.send("ginger"))
print(stall.send("cardamom"))
