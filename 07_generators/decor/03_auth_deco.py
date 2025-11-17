from functools import wraps
def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tes_inventory(role):
    print("Access granted to invento")

access_tes_inventory("user")
access_tes_inventory("admin")

