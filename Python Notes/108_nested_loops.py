# looping over embedded lists

normal_list = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3], [4, 5, 6]]

# for data in embedded_list:      # iterates over 1,2,3 and then prints them
#     print(data)
#     for num in data:        # iterates over 4,5,6 and then prints them
#         print(num)

dict_data = {1: {'name': 'stanley ho', 'money': 0.05},
              2: {'name': 'jeff bezzos', 'money': 0.08},
              3: {'name': 'stanley ho', 'money': 0.02}}
# objective is to output name of person, money *400,000,000)
# float(dict_data['money'].replace('$', '')

for i in dict_data:
    print(dict_data[i]['name'])
    print(dict_data[i]['money'] * 400000000)

