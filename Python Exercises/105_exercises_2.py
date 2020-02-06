# List basics :D
#1 - Define a bucket list with 10 items
#2 - Print the entire list
#3 - Check the length of the list / how many items inside the list?
#4 - print the first item
#5 - Prin the second item
#6 - add one more item to the list
#7 - prin the last item in the list
#8 - Re assign an item and print all of the list again

bucket_list = ['apple', 'bannana', 'carrot', 'tangerines', 'spinach', 'grapes', 'orange', 'raspberries', 'strawberries',
               'peppers']
print(bucket_list)
print(len(bucket_list))
print(bucket_list[0])
print(bucket_list[1])
bucket_list.append('brussel sprout')
print(bucket_list[-1])
bucket_list[1] = 'pears'
print(bucket_list)

# Dictionary basics :D
#1 - Define a dictionary call story1, it should have the followign keys:
        # start, middle and end
#2 - Print the entire dictionary
#3 - Print the type of your dictionary
#4 - Print only the keys
#4 - print only the values
#5 - print the individual values using the keys (individually, lots of printi commands)
#6 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero

story_dictionary = {'beginning': 'finds out about sauron', 'middle': 'travels to mordor',
                    'end': 'throws ring into mountain of doom', 'hero': 'Frodo baggins'}

print(story_dictionary)
print(type(story_dictionary))
print(story_dictionary.keys)
print(story_dictionary.values)
print(story_dictionary['hero'])
print(story_dictionary['beginning'])
print(story_dictionary['middle'])
print(story_dictionary['end'])

