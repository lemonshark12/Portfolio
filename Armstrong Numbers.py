import sys

def armstrong_choice():
	"""Code written to determine:
	[1] whether a number is an Armstrong Number (the sum of the cube of each digit equals the digit
		EXAMPLE: 1**3 + 5**3 + 3**3 = 153
	[2] a list of Armstrong Numbers in a provided range"""
	
	print("\nPlease select an option or type 'exit' to quit:\n[1] to check if a number is an Armstrong Number")
	print("\n[2] to show all Armstrong Numbers in a range")
	choice = input(">> ")
	
	if choice == 'exit':
		sys.exit("Thank you for using the Armstrong Number checker.  Have a great day!")
	elif choice == "1":
		check_number()
	elif choice == "2":
		find_inrange()
	else:
		print("Please make an appropriate selection")
		return armstrong_choice()
		
def check_number():
	number = input("Provide a number to check\n>> ")
	digit_list = []
	msg = ["It's an Armstrong Number!", "Not an Armstrong Number!"]
	for digit in number:
		digit_list.append(digit)
	#print (digit_list)
	
	if (int(digit_list[0])**3) +  (int(digit_list[1])**3) + (int(digit_list[2])**3) == int(number):
		print (msg[0])
		return armstrong_choice()
	else:
		print (msg[1])
		return armstrong_choice()
		
def find_inrange():
	msg = ["Please enter the starting value of the range to process\n>> ", "Please enter the ending value of the range to process\n>> "]
	start = input(msg[0])
	end = input(msg[1])
	
	def test_range(n,m):
		print ("using test_range function")
		test_range = []	
		for i in range(n, m+1):
			test_range.append(i)
		return (test_range)
		
	test_range = test_range(int(start), int(end))
	print (test_range)

	def split_number(n):
	#n = input(">> ")
		digit_list = []
		for digit in n:
			digit_list.append(digit)
			#	print (digit_list)
		return (digit_list)
		
	def cube_numbers(n):
		def cube_this(j):
			return j**3
		cubed_elements = list(map(cube_this, n))
		return (cubed_elements)
	
	def elementify_list(n):
		print ("printing n", n)
		digit_list = []
		for digit in str(n):
			digit_list.append(int(digit))
		return (digit_list)

	def sum_elements(n):
		return sum(n)

	def check_armstrong():

		digit_list = split_number(test_range) #this splits the provided test range data into a list where each li is a list of the digits of each previously whole li
		elemented_list = list(map(elementify_list, digit_list))
		cubed_list = list(map(cube_numbers, elemented_list))
		summed_list = list(map(sum_elements, cubed_list))
		armstrong_list = [] #this is where final answers will be stored
	
		for i in digit_list:
			if i == i in summed_list:
				armstrong_list.append(i)

				
		print ("this is the digit_list", digit_list)
		print ("this is elemented list", elemented_list)
		print ("this is cubed list", cubed_list)
		print ("This is the li I'm trying to sum", summed_list)
		print ("this is armstrong_set", armstrong_list)
		#print ("this is split_cubed_list", split_cubed_list)
		#return (cubed_list)
		
	check_armstrong()
	
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#SUMMING OF CUBED IS FUCKED UP.  CHECK WITH SMALLER RANGE.  FIX 3 DIGIT LIMITATION IN SEGMENT CHOICE #1
#------------------------------------------------------------------------------------------------------------------------------------------------------------




#	def split_number(tr):
#		print ("splitting numbers")
#		balls = []
#		for digit in tr:
#			return balls.append(digit)
		
#	def split_number(tr):
#		print ("using split_number function")
#		digit_list = []
#		for digit in tr:
#			digit_list.append(digit)
#		return (digit_list)
	
#	digit_list = list(map(split_number, test_range))
#	#digit_list = split_number(test_range)	
#	print (digit_list)
		
#	def cube_numbers(n):
#		print ("cubing the numbers")
#		return int(n)**3

#	def cube_list(test_range, digit_list):
#		print ("using cube_list funtion")
#		digit_list = split_number(test_range)
#		cubed_list = list(map(cube_numbers, digit_list))
#		print (cubed_list)
#		return (cubed_list)
		
#	def check_armstrong(cubed_list):
#		print ("using check_armstrong function")
#		for i in test_range:
#			cube_list(test_range, digit_list)
			
#			if sum(cubed_list) == i:
#				armstrong_list.append(i)
#				print (armstrong_list)
#				i += 1

			
			
		#armstrong_list = 
		#return (cubed_list)
	
#	check_armstrong(cubed_list)
		
		#if check_armstrong(test_range, digit_list) == True:
		#	armstrong_list.append(i)
	#print (armstrong_list)
	

#check_armstrong()		
armstrong_choice()