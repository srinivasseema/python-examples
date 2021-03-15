#Tuples, immutable list and cannot be modified...
dimensions = (200,50)
print(f'first tuple {dimensions[0]}')
print(f'second tuple {dimensions[1]}')

#dimensions[0] = 300, TypeError: 'tuple' object does not support item assignment
#single tuple, has a leading comma..
my_t=(4,)
# print tuples
for dimension in dimensions:
	print(dimension)