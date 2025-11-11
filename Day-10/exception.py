a = int(input())
b = int(input())

try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print('Dont enter zero in denominator')