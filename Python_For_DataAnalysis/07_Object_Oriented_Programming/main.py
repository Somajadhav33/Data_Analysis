class Smartphone: #With Constructor
    def __init__(self, brand, model, price): # Constructor
        self.brand = brand
        self.model = model
        self.price = price

    def show_info(self):
        print(f"{self.brand} {self.model} {self.price}")

iphone = Smartphone("Apple", "iPhone 15", 999)
pixel = Smartphone("Google", "Pixel 8", 799)
iphone.show_info()
pixel.show_info()

#incapsulation
class Smartphone2: #Without Constructor
    brand = "Apple"
    model = "iPhone 15"
    price = 999
    def show_info(self):
        print(f"{self.brand} {self.model} {self.price}")

iphone2 = Smartphone2()
iphone2.show_info()

#Abstraction

class Smartphone3:
    class_name = "Smartphone" #public
    def __init__(self, brand, model, price): # Constructor
        self.__brand = brand #private
        self.model = model #protected
        self.__price = price #private

    def show_info(self):
        print(f"{self.__brand} {self.model} {self.__price}")

smartphone3 = Smartphone3("Apple", "iPhone 15", 999)
smartphone3.show_info()
print(smartphone3.class_name)
# print(smartphone3.price) Error
# print(smartphone3.model) Error
print(smartphone3._Smartphone3__brand)
print(smartphone3._Smartphone3__price)

#inheritance
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"{self.name} {self.age}")

class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age) #calling parent class constructor
        self.school = school
    def show_info(self):
        print(f"Child Class : {self.name} {self.age} {self.school}")
        super().show_info() #calling parent class method

child = Child("John", 10, "ABC")
child.show_info()
