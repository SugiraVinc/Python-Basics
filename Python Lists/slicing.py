'''List slicing: accessing a limitted number of elements'''
""" syntax:listname[start_index : end_index : step] """

my_list1 = [12, 40, 50.5, 'Kirenga', 'Amanda']
print(my_list1[2 : 5])

my_list = [10, 20, 'Jessa', 12.50, 'Emma', 25, 50]
# Extracting a portion of the list from 2nd till 5th element
print(my_list[2:5])


"""print every second element with a skip of two counts"""
print(my_list[::2])

"""Reversing a list"""
print(my_list[::-1])

# Without end_value - starting from nth item to last item

print(my_list[3:])