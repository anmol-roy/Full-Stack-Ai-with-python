class Chai:
    temp = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temp)

cutting.temp = "mild"
cutting.cup = "small"
print("After", cutting.temp)
print("cup size is", cutting.cup)
print("Direct look into the the class", Chai.temp)

del cutting.temp
del cutting.cup
print("After", cutting.temp)
print("After", cutting.cup)