# 2 - Write a function that retrieves an element from a list.

def element_at(my_list, idx):
    if idx < 0 or idx >= (len(my_list)):
        return None
    else:
        return my_list[idx]
my_list = [1, 2, 3, 9, 5]
item = element_at(my_list, 2)
print (item)

print ()

# 3 - Write a function that replaces an element of a list at a specific position

def replace_in_list(my_list, idx, element):
    #to not modify anything
    if idx < 0 or idx >= (len(my_list)):
        return my_list
    #to modify
    else:
        # remove element with index
        # add element by index
        my_list.pop(idx)
        my_list.insert(idx, element)
        return my_list
my_list = [1, 2, 3, 9, 5]
my_list = replace_in_list(my_list, 3, 4)
print(my_list)

print ()

# 4 - Write a function that prints all integers of a list, in reverse order.

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for element in my_list:
        print(element, end=" ")
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

print ()

# 5 - Write a function that replaces an element in a list at a specific position without modifying the original list.
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    #to return a copy of the original list
    if idx < 0 or idx >= (len(my_list)):
        return my_list
    #to modify
    else:
        # remove element with index
        # add element by index
        new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list


my_list = [1, 2, 3, 9, 5]
new_list = new_in_list(my_list, 3, 4)
print(my_list)
print(new_list)

print ()

# 6 - Write a function that finds the biggest integer of a list.

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        return my_list

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print (max(my_list))

print ()

# 7 - Write a function that adds 2 tuples.
def add_tuple(tuple_a=(), tuple_b=()):
    first_element = tuple_a[0] + tuple_b[0]
    second_element = tuple_a[1] + tuple_b[1]
    return first_element, second_element

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)



