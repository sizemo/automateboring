tD = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
	# figuring out how long the longest string in the list is
  colWidths = [0] * len(tableData)
	n = 0
	for i in tableData:
		eachList = []
		for x in i:
			eachList.append(len(x))
			biggest = max(eachList)
		colWidths[n] = biggest
		n += 1
  
  # I really wanted to do this by transforming the list items
  # but you're not really supposed to/able to do that, so I
  # created a new list of lists identical to the original input
  # and wrote the right justified list elements to that new list
	n = 0
	columnTab = tableData
	for i in range(len(tableData)): # to use this method you can't call a normal for loop on i in tableData
		for x in range(len(tableData[i])): # same here with a for x in i
			columnTab[i][x] = str(tableData[i][x].rjust(colWidths[n], ' ')) # because in this line it'll error for trying to use a non int or slice
		n += 1
	
  # getting the justified elements to print correctly
  # I repurposed the grid transforming code from a few chapters ago
	for s in range(4):
		for f in range(3):
			if f == 2:
				print(columnTab[f][s], end= '\n')
			else:
				print(columnTab[f][s], end= ' ')


printTable(tD)
