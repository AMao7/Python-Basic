# lists
crazy_landlords = []         # defining a list
print(type([crazy_landlords]))

# name_list =  [0, 1, 2, 3, 4, 5, 6]     # access object in a list through indexing
crazy_landlords = ['Richards', 'Raj', 'Harry']       # can dynamically a list or re-define a list

print(crazy_landlords[1])       # prints Raj
print(crazy_landlords[2])       # prints Harry
print(crazy_landlords)      # prints everything
print(crazy_landlords[-1])     # prints the last value, which is Harry in this case
length = len(crazy_landlords)
last_index = length - 1
print(last_index)       # prints the last value using len
crazy_landlords.append('Lana')      # use append to add a value to the list
crazy_landlords.insert(4, 'Jack')        # insert Jack to specific index
crazy_landlords.remove('Raj')       # removes Raj from list
crazy_landlords.pop()       # removes last index or specified index

# we can also redefine at a specific index
crazy_landlords[1] = 'Rajjesh'      # changes the 2nd string raj to rajjesh
print(crazy_landlords[0:2])     # 0 to 2, not including 2


hybrid_list = ['Jason', 1, 2, 'Abdimalik']      # we can have mixed data lists too!

my_tuple = (1, 'Hello', 2)      # Tuples are immutable lists
print(my_tuple[1][0])       # takes the first at the first character of Hello

example_list = [0, 1, 2, 3, 4, 5, 6] # jumping/slicing (N:S:M), where N is the start, S is where to stop and M is every jump (length)
print(example_list[0 :6 :2]) # starts from 0, skips 2 and stops at 6






