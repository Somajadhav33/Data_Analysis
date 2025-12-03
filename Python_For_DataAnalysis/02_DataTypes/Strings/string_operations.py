first_name = 'Somnath' #Single Quotes
last_name = "Jadhav" #Double Quotes

#String Operations
#  1. Concatenation - Combining two or more strings

full_name = first_name + " " + last_name 
print(full_name)

#  2. Repetition - Repeating String
five_star = "*" * 5
print(five_star)

#  3. Length
print(len(first_name))

#  4. Indexing 
text = "python"
print(text[0])
print(text[2])
print(text[-1]) #reverse indexing

#  5. Slicing - [start:end:step] - all are optional - slicing starts from start index and ends before one step of end index
print(text[1:4])
print(text[:4])
print(text[1:])
print(text[0:len(text):2]) # ignore two steps after indexing
print(text[::-1])
