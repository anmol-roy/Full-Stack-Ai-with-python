kettle_boiled = True
if kettle_boiled:
    print("Kettle is boiled. You can make tea.")
else:
    print("Kettle is not boiled. Please boil the kettle first.")


snacks = input("Enter your snack choice (cookies/samosa): ").strip().lower()
if snacks == "cookies" or snacks == "samosa":
    print("Order has been confirmed!")
else:
    print("We only serve cookies or samosa with chai.")