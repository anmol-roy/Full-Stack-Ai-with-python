class InvalidChaiError(Exception): pass

def bill (flavour, cups):
    menu = {"masala":20, "ginger": 40}
    try:
        if flavour not in menu:
            raise InvalidChaiError ("that chai is nor availsble")
        if not isinstance(cups, int):
            raise TypeError("number of cups must be in int")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} cups of {flavour} chai: rupees {total}")
    except Exception as e:
        print("Err",e)
    finally:
        print("thank u")

bill("mint", 2)
bill("mint", "two")
bill("ginger", 3)

