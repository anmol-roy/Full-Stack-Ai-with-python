def make_chai():
    ingredients = [
        "water",
        "milk",
        "black tea leaves",
        "sugar",
        "spices (like cardamom, cinnamon, ginger)"
    ]
    instructions = [
        "Boil water in a pot.",
        "Add black tea leaves and spices to the boiling water.",
        "Let it simmer for a few minutes.",
        "Add milk and sugar to taste.",
        "Bring the mixture to a boil again.",
        "Strain the chai into cups and serve hot."
    ]
    return ingredients, instructions
if __name__ == "__main__":
    ingredients, instructions = make_chai()
    print("Ingredients:")
    for item in ingredients:
        print(f"- {item}")
    print("\nInstructions:")
    for step_num, step in enumerate(instructions, start=1):
        print(f"{step_num}. {step}")