# for <placeholder> in <iterable>:
import time
cars = ['Skoda Felecia Fun', 'Mustang Boss 429', 'Fiat 500']

for i in cars:     # prints all iteration till it gets to the end
    print(i)
    time.sleep(0)

student1 = {'name': 'Arya Stark',
           'stream': 'Many Faces',
           'grade': 10
}
for i in student1:        # iterating over an dictionary (hash) or list (arrays)
    print(i)        # when you iterate a dictionary you get the key
    print(student1[i])      #


for i in student1:
    print(f"{i.capitalize()} is , {student1[i]}")


