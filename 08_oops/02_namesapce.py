class Chai:
    origin = 'india'

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# crating objects from class chai

masala = Chai()
print(f"Masla {masala.origin}")
print(f"Masla {masala.is_hot}")
masala.is_hot = False

print("Class :", {Chai.is_hot})
print(f"Masala {masala.is_hot}")

masala.flavour = "masala"
print(masala.flavour)