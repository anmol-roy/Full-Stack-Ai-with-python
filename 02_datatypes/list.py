# lists in python
my_list = ["milk", "eggs", "bread"]
print("Initial list:", my_list)
my_list.append("butter")
print("List after appending 'butter':", my_list)
my_list.remove("eggs")
print("List after removing 'eggs':", my_list)
print("Length of the list:", len(my_list))
nested_list = [["black tea", 5], ["milk", 10], ["sugar", 3]]
print("Nested list:", nested_list)
for item in my_list:
    print("Item:", item)    
for ingredient, quantity in nested_list:
    print(f"Ingredient: {ingredient}, Quantity: {quantity}")
# list comprehension
squared_quantities = [quantity ** 2 for ingredient, quantity in nested_list]
print("Squared quantities:", squared_quantities)    
# list slicing
print("First two items in my_list:", my_list[0:2])
print("Last two items in my_list:", my_list[-2:])
print("Items from index 1 to 2 in my_list:", my_list[1:3])

raw_spice_data = bytearray(b"cardamom,cinnamon,ginger")
print("Raw spice data (bytearray):", raw_spice_data)