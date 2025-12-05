l1 = [1, 2, 3, 4, 5]
# 1. Creating Tuples

t1 = (1, 2, 3)
t2 = ("apple", "banana", "mango")
t3 = (1, "mix", 3.5, True)
t4 = ()
t5 = (5,)  # single element donnt 
t6 = tuple(l1)

#Accessing 
print(t2[2])
print(t2[-1])
print(t2[1:3])

#Length
print(len(t2))

#Check Membership
print("apple" in t2 )
print("apple" not in t2 )

#concatenation
print(t1 + t2 + t3)

#Repetation
print(t2 * 3)

#count
print((t2*3).count("apple"))

#indexing
print(t2.index("apple"))

#Tuple Unpacking 

# a, b, c = t6 Error
a, b, c = t1
print(a, b, c)
