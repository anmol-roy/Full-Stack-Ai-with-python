def  my_deco(func):
    def wrapper():
        print("befor")
        func()
        print("after")
    return wrapper

@my_deco
def greet():
    print("hello from, deco class")

greet()