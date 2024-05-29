"""Use of append(), insert(), and extend"""

'''APPEND(): adds items at the end of the list'''
my_list = list((7,8.5, 'Tom', 7.50))
print('The original list is', my_list)

# append
my_list.append('Emma')
print('Appended : ', my_list, end =" ")
print(my_list)

# append the nested list at the end
my_list.append([25, 50, 75])
print(my_list)

print('----------------------------------------------------------------------')

'''Insert: insert(index, object)'''

my_list1 = list([5, 8, 'Tom', 7.50])
# Using insert()
# insert 25 at position 2
my_list.insert(2, 25)
print(my_list)

# insert nested list at at position 3
my_list.insert(3, [25, 50, 75])
print(my_list)

print('----------------------------------------------------------------------')

'''Extend(): accept list of elements and add them to the end of the list.'''

my_list = list([5, 8, 'Tom', 7.50])

# Using extend()
my_list.extend([25, 75, 100])
print(my_list)