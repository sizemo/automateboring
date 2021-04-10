aList = ['lions', 'tigers', 'bears']

def yesAnd(aList):
	aList.insert(-1, 'and')
	print(str(aList).strip('[]').replace("'", "").replace("and,", "and"))

yesAnd(aList)

