# introducing dictionaries!!
# dictionaries are organised using key value pairs, like a real dictionary
# inside here you will have a key pointing at a value
my_dictionary = {'name': 'Filipe', 'phone': '07842421'}


my_dictionary['address'] = 'Deptford', 'london'    # create one key value pair
print(my_dictionary['phone'])       # read one entry in a dictionary
my_dictionary['phone'] = '07482348382'      # update the value in a key
my_dictionary.pop('address')            # destroy one key value

keys = my_dictionary.keys()
print(keys)
values = my_dictionary.values()
print(values)

student1 = {
    'name': 'Morty',
    'stream': 'Universal quest',
    'grade': 12
}

student2 = {
    'name': 'Summer',
    'stream': 'Terrestrial quest',
    'grade': 20
}

students_list = [student1, student2]
print(students_list[1])

students_dict = {
            'student1': student1,
            'student2': student2
}
print(student1['name'])
print(student2['name'])


print(students_dict['student1']['name'])
print(students_dict['student2']['name'])