numbers = [1, 2, 3, 4, 5, 5]
tuple1 = (1, 4, 3, 4, 4)

#Creating sets
s1 = set(numbers)  #Removes Duplicates automatically
s2 = set(tuple1)
s3 = {1, 2, 3, 4, "a", "b"}
print(s1)
print(s2)
print(s3)

#Operations And Methods
print(len(s3))
s3.add("d")
print(s3) #Add single element
s3.update("e", "f", "g") #Add Multiple Elements
print(s3)

s3.remove("d")
# s3.remove("z") //Error if not found
# print(s3)
s3.discard("z") #no error if not found
s3.pop() #pop first element
print(s3)
print(s3.pop()) # return poped element

s3.clear() #remove all elements from set
print(s3)

#Membership Test

print(5 in s1)
print(5 not in s1)

#Mathematical Ops
s5 = {4, 5, 6, 7, 8}
s7 = {7, 8, 9, 10}
print(s5 | s7) #Union

print(s1 & s2) #Intersection
print(s1 - s2) #or s2 - s1 Diffrence
print(s1 ^ s2)

s6 = s2.copy() # Copy Sets
print(s6)

#Frozenset - Immutable Sets
frozen = frozenset([1, 2, 3, 4])
# frozen.add("q") Error
print(frozen)
