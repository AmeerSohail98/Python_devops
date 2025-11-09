# unpacking the dynamic variables
# a, b, c ,d = tuple(map(int, input().split()))
# print(a)
# print(b)
# print(c)
# print(d)

#List comprehension
lst2 = [x for x in range(0,3)]
print(lst2)

#tuple comprehension
tup2 = tuple(x for x in range(0,3)) 

'''Python does not have a direct syntax for tuple comprehension. The expression (x for x in range(5)) is a generator expression, 
which produces a generator object, not a tuple. that's why we need to include tuple constructor also in there for it''' 

print(tup2)

#Set comprehension
st1 ={x for x in range(0,3)}
print(st1)