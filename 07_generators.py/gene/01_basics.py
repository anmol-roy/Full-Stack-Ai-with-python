def serve_chai():
    yield "Boil water"
    yield "Steep tea leaves"
    yield "Add milk and sugar"
    yield "Serve chai"


stall = serve_chai()
for step in stall:
    print(step)

def get_step():
    return ["cup 1", "cup 2", "cup 3"]

def get_step_gen():
    yield "Boil water"
    yield "Steep tea leaves"
    yield "Add milk and sugar"
    yield "Serve chai"

chai = get_step_gen()
print(chai)