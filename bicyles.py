bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
print(bicycles[-2])

message = f'My first bicycle was a {bicycles[0].title()}'
print(message)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('newmodel')
print(motorcycles)


motorcycles.insert(4, 'Honda')
print(motorcycles)

#del keyword, to delete an item from a list
del motorcycles[3]
print(motorcycles)

#Removes the last element from list
first_owned = motorcycles.pop()
print(motorcycles)

first_owned = motorcycles.pop(0)
print(motorcycles)

# to remove an item by value, remove() method deletes only first occurence of element.

motorcycles.remove('Honda')
print(motorcycles)