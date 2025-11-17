def brew_chai(flavour):
    if flavour not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Unsupported chai flavour")
    print(f"Brewing {flavour} chai... ")


brew_chai("mint")
