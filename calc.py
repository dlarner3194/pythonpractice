def welcome():
	print('''
Welcome to the Calculator program!
''')

def calculate():
	operation = raw_input('''
Please type the math operation you would like:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

	number_1 = int(input('What is your first number: '))
	number_2 = int(input('What is your second number: '))

	if operation == '+':
		print ('{} + {} = '.format(number_1,number_2))
		print (number_1 + number_2) #addition

	elif operation == '-':
		print ('{} - {} = ').format(number_1,number_2)
		print (number_1 - number_2) #subtraction

	elif operation == '*':
		print ('{} * {} = ').format(number_1,number_2)
		print (number_1 * number_2) #multiplication

	elif operation == '/':
		print('{} / {} = ').format(number_1,number_2)
		print (number_1 / number_2) #division

	else:
		print ('You messed something up bruh.')

	again()

def again():
	calc_again = raw_input('''
Do you want to calculate anything else?
Type Y for yes and N for no
''')

	if calc_again.upper() == 'Y':
		calculate()
	elif calc_again.upper() == 'N':
		print('Thank you for your time.')
	else:
		again()

welcome()
calculate()



