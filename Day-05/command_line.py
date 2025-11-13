import sys

'''now if i want to provide inputs when i am calling the python file name in the terminal then we use sys module to read those inputs this is 
known as command line arguments'''

def addition(a,b):
    ad= (a+b)
    return ad

def sub(a,b):
    s =(a-b)
    return s

def mul(a,b):
    m= (a*b)
    return m

def div(a,b):
    d = (a//b)
    return d

'''Now in this program we have two inputs to give and four operations to perfrom so they need 3 arguments to capture when we are instructing 
python file in command terminal'''

num1 = int(sys.argv[1]) #This represents the order of the inputs we are providing in the command terminal
operation = sys.argv[2] # This is calculator program this represents the data of operation to perform
num2 = int(sys.argv[3]) #This represents the order of the inputs we are providing in the command terminal

if operation == '+':
    output=addition(num1, num2)
    print(output)
elif operation == '-':
    output=sub(num1, num2)
    print(output)
elif operation == '*':
    output=mul(num1, num2)
    print(output)
elif operation == '/':
    output=div(num1, num2)
    print(output)
else:
    print('Invalid operation')