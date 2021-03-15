#IfStatementList
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers now.")
	else:
		print(f"Adding {requested_topping}.")
print("finished making your pizza")

# Check list is not empty:

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}")
	print("finished making pizza")
else:
	print("Are you sure you want a plain pizza!")

#Check requested toppings list available in available list

requested_toppings = ['mushrooms','french fries','extra cheese']
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding requested topping {requested_topping}")
	else:
		print(f"Sorry, we don't have requested topping {requested_topping}")
print("finished making your pizza")

