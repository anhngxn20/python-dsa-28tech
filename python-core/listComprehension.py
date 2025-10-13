# Structure: L = [expression for item in iterable]
# for x in range(1,5): print(x) --> l1 = [print(x) for x in range(1,5)]

l1 = [print(x) for x in range(1, 5)]

v = [0 for i in range(5)]
print(v)

l3 = [x.lower() for x in 'PyTHoN']
print(l3)

l5 = [x for x in '3a*3@b8ecd' if x.isalpha()]
print(l5)