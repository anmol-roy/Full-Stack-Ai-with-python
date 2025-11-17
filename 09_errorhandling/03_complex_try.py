def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai..")
        if flavour == "unknown":
            raise ValueError("we don't know that flavour")
    except ValueError as e:
        print("Error", e)
    else:
        print(f"{flavour} chai is served")
    finally:
        print("next custmer please!")

# serve_chai("masala")
serve_chai("unknown")