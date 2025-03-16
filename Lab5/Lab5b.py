from Dogs import Doggos

p1 = Doggos("Regi", 6,"John Dennis")
print(f"Name: {p1.name}, Age: {p1.age}, Owner: {p1.owner}")

p1.name = "Spot"
p1.age = 8
p1.owner = "Marie woods"

print(f"Updated Name: {p1.name}, Updated Age: {p1.age}, Updated owner: {p1._owner}")