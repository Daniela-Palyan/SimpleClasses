# Create a class named Car with no methods or attributes. 
# Then, create an instance of this class and print the type of the instance.
# Modify the Car class to accept brand and model as parameters during object creation. 
# Then, create an instance and print the attributes.
# Extend the Car class by adding a method display_info() that prints the brand and model of the car.
# Modify the Car class to have a default value for the model ("Unknown"). If the model is not 
# provided during initialization, it should use the default value.

class Car:
    def __init__(self, brand, model = 'Unknown'):
        self.__brand = brand
        self.__model = model

    def set_model(self, model):
        self.__model = model

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model
    
    def get_brand(self):
        return self.__brand

    def display_info(self):
        print(self.get_brand(), self.get_model())

# c1 = Car()
# print(type(c1))

c2 = Car('Opel', 'Astra')
print(c2.get_brand(), c2.get_model())

c3 = Car('BMW')
c3.display_info()