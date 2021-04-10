import random
numberOfStreaks = 0
sixHeads = ['h', 'h', 'h', 'h', 'h', 'h']
sixTails = ['t', 't', 't', 't', 't', 't']

for experimentNumber in range(10000):
	# Code that creates a list of 100 'heads' or 'tails' values
	bottom = 0
	top = (bottom + 6)
	str_ref = []
	headsOrTails = [] 
	i = 0
	for i in range(100):
		theFlip = random.randint(0, 1)
		if theFlip == 0:
			headsOrTails.append('h')
		else:
			headsOrTails.append('t')


# Code that checks if there is a streak of 6 heads or tails in a row

	for iterat in headsOrTails:
		str_ref.append(headsOrTails[bottom:top])
		bottom += 1
		top += 1
		
	if sixHeads in str_ref:
		numberOfStreaks += 1
	elif sixTails in str_ref: 
			numberOfStreaks += 1
	else:
		pass

print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
