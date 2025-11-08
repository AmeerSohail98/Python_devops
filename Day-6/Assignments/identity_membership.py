#Task 6: Identity and Membership Operators
my_list = ['apple', 12, 32.4, "orange"]
#Identity Operators
a = my_list
b = ['apple', 12, 32.4, "orange"]

is_same_object = a is my_list #True
is_not_same_object = b is not my_list #True

# Membership operators
element_in_list = 12 in my_list
element_not_in_list = 'grapes' not in my_list

print("a is my_list:", is_same_object)#True
print("b is not my_list:", is_not_same_object)#True
print("12 in my_list:", element_in_list)#True
print("grape not in my_list:", element_not_in_list)#True