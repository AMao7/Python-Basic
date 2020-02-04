# strings in python
# strings are lists of characters put together in a list

# defined by '' or ""

my_string = "Amazing grilled fish"
print(type(my_string))

# Joining of two strings
first_name = 'Boris'
last_name = 'May'

print(first_name + ' ' + last_name)     # you can add them and save them as different variable
full_name = first_name + last_name
print (full_name)       # you can also create a new defined variable

# Interpolation
# you inject a string into another string
name = 'Lana'
welcome_message = "welcome to the dangerzone!"
print(f"{name *10}, welcome to the dangerzone!")     # place an f behind the string and use {} inside the string

my_string = "Hello this is an amazing string"

print(my_string.count('i'))     # .count() to count the amount of letters
print(my_string.strip())      # removes whitespace
print(len(my_string))       # len is a function that counts characters
print(len(my_string.strip()))       # strips and then counts characters
print(my_string.strip().capitalize())
print(my_string.strip().upper())
print(my_string.strip().lower())
print(my_string.strip().split   ())
