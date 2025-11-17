def infinite_chai():
    count = 1
    while True:
        yield f"refil {count}"
        count += 1

refil = infinite_chai()
use2 = infinite_chai()

for _ in range(5):
    print(next(refil))

for _ in range(3):
    print(next(use2))