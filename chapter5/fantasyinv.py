stuff = {}

# I thought it wasn't very useful to have to define the string in the script
# so I went ahead and wrote something that allows you to input the items up
# front. I'd like to make it so that you don't have to write "s, i" to save
# and can just type "s" or "save" but I couldn't figure out how to deal with
# the split I needed to get this to work handling a single command.

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

# Building the function to display the items as directed in the problem

def invDisplay(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total = item_total + v
	print('Total number of items: ' + str(item_total))
		
invDisplay(stuff)		
