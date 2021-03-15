#Dictionaries, dictionaries keeps the order of the elements
alien_0 = {'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Setup coordinates
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_1 = {'color': 'green'}
print(f"The alien color is {alien_1['color']}")
alien_1['color']='yellow'
print(f"The alien color is now {alien_1['color']}")

# Removing key-value pairs from dictionary:

del alien_0['points']
print(alien_0)

#Multi line dictionary:
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

print(favorite_languages)

# Sarah's favorite language
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language {language}")


#Access if key doesn't exist
#print(alien_0['points'])
# output KeyError: 'points'

#Use get method to return default value if the requested value doesn't exist..
print(alien_0.get('points',0))
print(alien_0.get('points')) # Returns None without second argument

#Iteration through Dictionary:
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'lastname': 'fermi',
}

for k, v in user_0.items():
	print(f"\nKey: {k}")
	print(f"Value: {v}")

#Just names of the people who took poll for the language:
for name in favorite_languages.keys():
	print(name.title())

for name in favorite_languages:
	print(name.title())

#Looping through dictionary's keys in particular order
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

#Looping through the dictionary's values
print("\n")
for language in favorite_languages.values():
	print(language.title())

#values may have duplicates, to get the unique elements from values, we need to convert values to set
# A set is a collection in which each item must be unique.
print("\nUnique languages: ")
for language in set(favorite_languages.values()):
	print(language.title())

# A list of dictionaries

alien0 = {'color': 'green', 'points': 5}
alien1 = {'color': 'yellow', 'points': 10}
alien2 = {'color': 'red', 'points': 15}

aliens = [alien0, alien1, alien2]
for alien in aliens:
	print(alien)














