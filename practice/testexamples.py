'''
1st example
a=2
a=4
print(a)
a=6
print(a)
print(a+a+a)

2nd example
a = 1
b = 2
print(a == b)
print(b == c)



a = "1"
b = 2
print(int(a) + b)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[1])
print(letters[3:6])
print(letters[:3])
print(letters[-2])
print(letters[-3:])
print(letters[::2])

'''


#Ranges
my_range=range(1,21)
print(list(my_range))
for i in my_range:
   print(10*i)

print([10*i for i in my_range])
print(list(map(str, my_range)))

a = ["1", 1, "1", 2]
b=set(a)
print(b)

a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

d = {"a": 1, "b": 2}
print(d(b).value)