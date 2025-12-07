#Basic Input

# name= input("Enter An Number: ")
# print(f"Hello {name } !")

# age = int(input("Enter age : "))#converting input to int
# print(f" Your Age Is : {age}")

# marks = float(input("Enter marks(%) : "))#converting input to float
# print(f" Your marks are : {marks}")


#Using Split()

# a, b = map(int, input("Enter Two Numbers: ").split(","))
# print(a + b)

# x, y, z = [int(x) for x in input("Enter 3 nums: ").split()]
# print(x + y +z)

#List Comprehension
numbers = [int(x) for x in input("Entered numbers : ").split()]
print(f"You entered -  {sum(numbers)}")

