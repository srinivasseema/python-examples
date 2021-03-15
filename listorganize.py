#Organizing list, sort method sorts the list permanently.

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)


#Sorting a list temorarily, use sorted() function

print(sorted(cars))
print(f"original order {cars}")

cars1 = ['bmw1','audi1','toyota1','subaru1']
print(sorted(cars1, reverse=True))

# To reverse the order of the list, instead of sorting and it does permanently
cars1.reverse()
print(cars1)

# Find the length of the list
print(len(cars1))