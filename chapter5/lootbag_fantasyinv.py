import random
import time

# Went above and beyond on this one too. Instead of defining the loot bag in a list,
# I wanted to create a list of things that could be in the loot drop and create a 
# random set of items each time the script ran. loot_roll contains all of the items
# that the loot bag can contain.

stuff = {}
loot = []
loot_roll = ['gold', 'rune dagger', 'uncut ruby', 'adamant full helm', 'dragon bones', 'prayer potion', 
             'numulites', 'mahogany logs', 'coal ore', 'iron ore', 'fishing explosives', 'ice gauntlets',
            'bird house', 'apple tree seed', 'willow seed', 'maple seed']

# The following code allows you to input the items already in your inventory, same as the first one

while True:	
	print('Enter item and quantity separated by a comma to add to your inventory or s, i save inventory.')
	item, quantity = input().split(',')
	if item == 's':
		break
	if item not in stuff:
		try: 
			stuff[item] = int(quantity)
		except:
			print('Please remember to use a comma to separate the two.')

# This part is where the script selects five items from the loot_roll list
# Note that per the instructions in the book, the code can select an item
# more than once.

while True:
	for i in range(5):
		drop = random.choice(loot_roll)
		loot.append(drop)
	break

# Just wanted to have some fun with this part and make it like a video game  
  
time.sleep(1)

print('...')
print('You stumble upon a dropped loot bag!')

time.sleep(1)

print('You open the bag and add the following items to your inventory!')
print(loot)
print('\n')

time.sleep(5)

#Adding the loot bag items to your inventory, accounting for duplicates

def addToInventory(inventory, addedItems):
	for item in addedItems:
		if item not in inventory:
			inventory[item] = 1
		else:
			inventory[item] = inventory[item] + 1
		
addToInventory(stuff, loot)		

# Turning the dictionary into the printed strings like before

def invDisplay(inventory):
	print("Your inventory now contains: \n")
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total = item_total + v
		
		
	print('Total number of items: ' + str(item_total))
		
invDisplay(stuff)		
