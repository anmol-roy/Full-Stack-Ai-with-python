# set in python
essential = {"salt", "pepper", "turmeric"}
optional = {"cumin", "coriander"}
print("Essential spices:", essential)
print("Optional spices:", optional)
all_spices = essential | optional
print("All spices:", all_spices)

common = essential & optional
print("Common spices:", common)

only_essential = essential - optional
print("Only essential spices:", only_essential)

print("Is 'cumin' an essential spice?", "cumin" in essential)


