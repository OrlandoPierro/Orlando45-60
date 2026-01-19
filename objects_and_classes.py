# object = A "bundle" of related attributes (variables) and method (functions)
# class = (bluebrint) used to design the structure and layout of an object

class Car:  # by convention classes are capitalized
    def __init__(self, model, year, color, for_sale): # initiliazing method for objects
        self.model = model  # we assing to the attribute model in the self the value model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):    # method that when called will execute the code below
        print(f"You drive the {self.model}")    #self.model acces to the model attribute of the object

car1 = Car("Mustang", 2024, "red", False)   # we initialize an object as it was a function

print(car1) # prints the memory address at which the object is located
print(car1.year)    # dot is the attribute access operator, this will print the content of the attribute year
car1.drive()    # calls the method drive