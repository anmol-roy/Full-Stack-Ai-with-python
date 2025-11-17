class ChaiCup:
    size = 150 

    def desccribe(self):
        return f"A {self.size} ml chai cup"


cup = ChaiCup()
# print(cup.desccribe())
print(ChaiCup.desccribe(cup))

cup_two = ChaiCup()
cup_two.size = 100
print(ChaiCup.desccribe(cup_two))