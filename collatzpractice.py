def collatz(number):
	global output
	if (number % 2 == 0):
		output = number // 2
		print(output)
	else:
		output = 3 * number + 1
		print(output)
	
try:
		while True:
			print('Input your number')
			chosen = int(input())
			collatz(chosen)
			while output != 1:
				collatz(output)

except ValueError:
	print('Please enter an integer instead.') 
				
