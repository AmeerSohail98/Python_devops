# All dictionary programs
#create a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)

#Access the name from dictionary data
print(my_dict['name'])

#modifying values
my_dict['age']=26
my_dict['occupation']='Engineer'
print(my_dict)

#Removing elements form dictionary
del my_dict['age']
print(my_dict)

#Checking key existence
if 'city' in my_dict:
    print('the key value is available in the dictionary')

#Using for loop on the dictionary data 
for k, v in my_dict.items():
    print(k)
    print(v)