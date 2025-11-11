# dictionary
my_dict = {"milk": 2, "eggs": 12, "bread": 1}
print("Initial dictionary:", my_dict)
my_dict["butter"] = 1   
print("Dictionary after adding 'butter':", my_dict)
del my_dict["eggs"]
print("Dictionary after removing 'eggs':", my_dict)
print("Number of items in the dictionary:", len(my_dict))

# printing keys
for item in my_dict:
    print("Item:", item)
# printing keys and values
for item, quantity in my_dict.items():
    print(f"Item: {item}, Quantity: {quantity}")

# dictionary comprehension
squared_quantities_dict = {item: quantity ** 2 for item, quantity in my_dict.items()}
print("Squared quantities dictionary:", squared_quantities_dict)