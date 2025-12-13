# Control Statements in Python
fruits = ["apple", "banana", "cherry"]

# 1. Conditional statements
n = 10
if n < 5:
    print(f"{n} is less than 5")
elif n == 5:
    print(f"{n} is equal to 5")
else:
    print(f"{n} is greater than 5")

# 2. Looping statements
# a. For loop
for i in range(0, 5):
    print(f"Iteration {i}")

for fruit in fruits:
    print(f"I like {fruit}")

# b. While loop
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

#Infinite loop 
# while True:
#     print("This will run forever unless interrupted.")


# 3. Control flow statements
# a. Break statement
for fruit in fruits:
    if fruit == "banana":
        print("Found banana, breaking the loop.")
        break
    print(f"Current fruit: {fruit}")    

# b. Continue statement
for fruit in fruits:
    if fruit == "banana":
        print("Skipping banana.")
        continue
    print(f"Current fruit: {fruit}")

# c. Pass statement
for fruit in fruits:
    if fruit == "banana":
        pass  # Placeholder for future code
    else:
        print(f"Current fruit: {fruit}")