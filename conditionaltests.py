#Conditional Tests
car = 'subaru'
print(car == 'subaru')
print(car != 'audi')
print(car == 'audi')

age = 17
if age >= 18:
	print("you are old enough to vote!")
else:
	print("Sorry, you are too young to vote")

#Amusement admission fee
age = 12
if age < 4:
	print("your admission cost is $0.")
elif age < 18:
	print("your admission cost is $25.")
else:
	print("your admission cost is $40.")
