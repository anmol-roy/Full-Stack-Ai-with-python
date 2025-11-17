fav_chais = [
    "Masala Chai",
    "Ginger Chai",
    "Masala Chai",
    "Tulsi Chai",
    "Elaichi Chai",
    "Ginger Chai",
]

unique_chais = {chai for chai in fav_chais}
# print(unique_chais) 

unique_chai = {chai for chai in fav_chais if len(chai) > 10}
# print(unique_chai)


recipes = {
    "Masala Chai": ["Tea Leaves", "Milk", "Sugar", "Spices"],
    "Ginger Chai": ["Tea Leaves", "Milk", "Sugar", "Ginger"],
    "Tulsi Chai": ["Tea Leaves", "Milk", "Sugar", "Tulsi Leaves"],
    "Elaichi Chai": ["Tea Leaves", "Milk", "Sugar", "Cardamom"],
}

unique_spices = { spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices) 