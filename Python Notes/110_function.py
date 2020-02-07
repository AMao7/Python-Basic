# Functions

# functions do one small task --> makes them testable
# it makes you code more readable, maintaniable and testable
# functions are like machines and can take inputs optionally
# DRY == Dont Repeat Yourself
# syntax is def<name>(arg, arg2):
# block of code
    # return, generally do not print

def say_hello():
    return 'hello'      # want function to hand arguments to another argument
print(say_hello())      # calling function with print

def full_name(f_name, l_name):      # takes two argument
    return f_name + ' ' + l_name        # the arguments action

print(full_name('abdimalik', 'mao'))        # function called

def welcome_message(f_name, l_name):
    full_name_str = full_name(f_name, l_name)
    welcome_str = say_hello()
    return welcome_str + ' ' + full_name_str

print(welcome_message('Abdimalik', 'Mao'))

#from <file name> import * (all) # imports all functions from filename, only call functions here