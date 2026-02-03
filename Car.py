# Create a class named Car with no methods or attributes. 
# Then, create an instance of this class and print the type of the instance.
# Modify the Car class to accept brand and model as parameters during object creation. 
# Then, create an instance and print the attributes.
# Extend the Car class by adding a method display_info() that prints the brand and model of the car.
# Modify the Car class to have a default value for the model ("Unknown"). If the model is not 
# provided during initialization, it should use the default value.

class Car:
    def __init__(self, brand, model = 'Unknown'):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(self.brand, self.model)

# c1 = Car()
# print(type(c1))

c2 = Car('Opel', 'Astra')
print(c2.brand, c2.model)

c3 = Car('BMW')
c3.display_info()