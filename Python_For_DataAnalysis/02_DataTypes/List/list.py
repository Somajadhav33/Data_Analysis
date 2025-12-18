# Create list
cars = ["BMW", "Tesla", "Audi", "Ford"]

# Access
print(cars[1])        # Tesla
print(cars[-1])       # Ford

# Modify
cars[1] = "Mercedes"

#iterate
for i in cars:
    print(i)

# Add items
cars.append("Honda")
print(cars)
cars.insert(0, "Lamborghini")
cars.extend("Suzuki")
print(cars)
print(len(cars))

# Remove items
cars.remove("Ford")

last = cars.pop() 
cars.clear()          # Empty list
print(cars) 
del cars
print(cars)    # Removes and returns last item

# Useful operations
numbers = [5, 2, 8, 1, 9]
numbers.sort()                    # [1, 2, 5, 8, 9]
numbers.reverse()                 # [9, 8, 5, 2, 1]
print(numbers.count(5))           # 1
print(8 in numbers)               # True

# List comprehension (Pythonic way)
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, ...]
evens = [x for x in range(20) if x % 2 == 0]