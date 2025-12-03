
#Case Conversion
text = "SoMnaTh jAdhav"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

#Whitespace & Cleaning
text2 = "  Hello World  "

print(text2.strip())
print(text2.lstrip())
print(text2.rstrip())
print("Mr.John".removeprefix("Mr."))
print("img.png".removesuffix(".png"))

#Searching & Checking


print("hello".find("ll"))       # 2
print("hello".rfind("l"))       # 3
print("hello".index("lo"))      # 3
print("banana".count("a"))      # 3
print("python.py".startswith("py"))  # True
print("photo.jpg".endswith(".jpg"))  # True


# Content Testing (True/False)

print("abc".isalpha())      # True
print("123".isdigit())      # True
print("abc123".isalnum())   # True
print("hello".islower())    # True
print("HELLO".isupper())    # True
print("Hello World".istitle())  # True
print("   ".isspace())      # True


# Modification & Replacement

print("I like cats".replace("cats", "dogs"))
# "I like dogs"

print("a,b,c".split(","))
# ['a', 'b', 'c']

print("-".join(['a', 'b', 'c']))
# "a-b-c"

print("hello-world".partition("-"))
# ('hello', '-', 'world')

print("py".center(10, "*"))
# "****py****"


print("hi".ljust(10, "."))  
# "hi........"

print("hi".rjust(10, "."))  
# "........hi"

#String Formating
name = "Soma"
age = 21

# f-string (Python 3.6+)
print(f"Hello {name}, you are {age} years old.")

# .format() method
print("Hello {}, you are {}.".format(name, age))

