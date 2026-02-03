# Create a class Person with attributes name and age. Create three instances of this class and store them in a list. 
# Then, loop through the list and print each person's information.

class Person:
    def __init__(self, name, age):
        if not isinstance(age, int):
            raise "Your age must be an integer number!"
        if age < 0:
            raise "Your age must be a positive number!"
        
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if not isinstance(age, int):
            raise ValueError("Your age must be a positive number!")
        
        self.__age = age
        
p1 = Person('Dany', 19)
p2 = Person('Ruzanna',8)
p3 = Person('Sasha', 25)
ls = [p1, p2, p3]

for person in ls:
    print(person.get_name(), person.get_age())