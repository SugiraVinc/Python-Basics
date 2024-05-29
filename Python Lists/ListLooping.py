my_lists = list((5, 79, 'Patrick', 70.4, 'Shema', 'Zook'))
for item in my_lists:
    '''if item == 79:
        break'''
    
    print(item)

"""Iterate with index and range function"""

print("Iterating a list by indexing")
my_list = [5, 8, 'Tom', 7.50, 'Emma']

# iterate a list
for i in range(0, len(my_list)):
    # print each item using index number
    print(my_list[i])