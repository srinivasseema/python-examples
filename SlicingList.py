#Slicing a list:
players = ['charles','martina','michael','florence','eli']
#To print first 3 players of list
print(players[0:3])
# To print from 1 to 4(exclusive)
print(players[1:4])
#To print elements from the last
print(players[-3:])

# Loop
for player in players[:3]:
	print(player.title())

# To copy list
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print("\n")

for friend in friend_foods:
	print(friend)

