class OutofingredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutofingredientsError("Missing milk or sugar")
    print("chai is ready")