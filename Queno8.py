# Write a python program to Sort a tuple of tuples by the second item.
tuple1= (('a', 21),('b', 37),('c', 11), ('d',29))
tuple2= tuple(sorted(tuple1, key=lambda item: item[1]))
print(tuple2)