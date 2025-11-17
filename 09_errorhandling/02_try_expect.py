chai_menu = {"masla": 30, "ginger": 40}
try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are trying to accesss does not exist ")

print("hello world!")