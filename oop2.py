class parrot:
    #class atribuit(variable inside a class)
    species= "bird"

    #constructor
    def __init__(self, name, age):
       self.name = name
       self.age = age

#create objects
parrot1 =parrot("blue","5")
parrot2 =parrot("woo","10")

#print their info
print("\n parrot1" )
print("name:", parrot1.name)
print("age:", parrot1.age)
print("species:", parrot1.species)

print("\n parrot2" )
print("name:", parrot2.name)
print("age:", parrot2.age)
print("species:", parrot2.species)