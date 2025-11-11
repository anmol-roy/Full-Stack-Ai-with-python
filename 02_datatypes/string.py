chai_type = "Masala Chai"
customer_name = "Anmol"

print(f"order for {customer_name}: {chai_type} please!")
# inexing 
first_letter = chai_type[0]
print("First letter of chai type:", first_letter)
last_letter = customer_name[-1]
print("Last letter of customer name:", last_letter)
middle_letter = chai_type[len(chai_type) // 2]
print("Middle letter of chai type:", middle_letter)
# string slicing
print("First three letters of chai type:", chai_type[0:3])
print("Letters from index 2 to 5 of customer name:", customer_name[2:6])
print("Last four letters of chai type:", chai_type[-4:])

# encoding and decoding
encoded_chai = chai_type.encode("utf-8")
print("Encoded chai type:", encoded_chai)
decoded_chai = encoded_chai.decode("utf-8")
print("Decoded chai type:", decoded_chai)
