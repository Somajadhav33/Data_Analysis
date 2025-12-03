#Single Line Comments - starts with #
name = "Somnath" #Assign a string to the variable

#Multiline comments  (''' or """)

'''
This is multiline comments 
You can write as many lines you want
'''

"""
Also we can use doube quotes
It work similar to the single quotes
"""

#Docstrings - Docstrings are special multi-line comments placed right after a function, class, or module definition.

def add_Numbers(a, b):
    """
    Add two numbers and return the result.

    Parameters:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    """
    return a + b;

print(add_Numbers(11, 34))


