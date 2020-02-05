# Numerical data types
## These are ints, long, float, complex
## These are numerical types which can use numerical operators

## Complex and long, and is built with imaginary numbers
    ## e.g if you would need to keep track of two different currencies

## Long are just integers of unlimited size

# ints and floats
# int - stands for integers and they are whole numbers
# floats - numbers with decimal places

my_int = 10
print(my_int)
print(type(my_int))

my_float = 10.0
print(my_float)
print(type(my_float))

# Operators - Add, subtract, divide, multiply and modulus
num1 = 12
num2 = 21

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print(10 % 3)     # modulus returns the remainder
print(10 // 3)      # removes the decimals and rounds

# Comparison Operators --> Boolean values
## to compare something use == (equating things on both sides)
## < / > lower or greater than
## <= >= lower/equal or greater/equal
## != not equal to
## is equates if something is something
## is not equates if something is not something

my_variable = 10
my_variable2 = 13

print(my_variable == my_variable2)
print(my_variable == 10)
print(my_variable < my_variable2)

# booleans are true or false
# they are binary
# none does not exist

# Operators, Logical and Logical Or
a_var = True
b_var = False

print(a_var & True)
print(a_var & False)        # Logical and & requires both sides to be true to remain true
print(True or False)        # Logical or requires one side to be true to remain true
