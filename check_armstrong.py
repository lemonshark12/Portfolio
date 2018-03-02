#test_range = [1, 23, 153, 156, 234, 556, 2277, 371, 370, 372, 407, 409, 512]
	
	
def define_test_range():	
	test_range = []
	msg = ["Please enter the starting value of the range to process\n>> ", "Please enter the ending value of the range to process\n>> "]
	start = input(msg[0])
	end = input(msg[1])
	for i in range(int(start),int(end)+1):
		test_range.append(i)
	print (test_range)	
#	test_range = test_range((int(start)),(int(end)))
	return (test_range)
	
#def test_range(n,m):
#	print ("using test_range function")
#	test_range = []	
#	for i in range(n, m+1):
#		test_range.append(i)
#	return (test_range)
		
#test_range = test_range(int(start), int(end))

#return (test_range)

#def split_number(n):
	#n = input(">> ")
#	digit_list = []
#	for digit in n:
#		digit_list.append(digit)
#	print (digit_list)
#	return (digit_list)
		
def cube_numbers(n):
	def cube_this(j):
		return j**3
	cubed_elements = list(map(cube_this, n))
	return (cubed_elements)
	
def elementify_list(n):
#	print ("printing n", n)
	digit_list = []
	for digit in str(n):
		digit_list.append(int(digit))
	return (digit_list)

def sum_elements(n):
	return sum(n)


def check_armstrong():
	test_range = []
	msg = ["Please enter the starting value of the range to process\n>> ", "Please enter the ending value of the range to process\n>> "]
	start = input(msg[0])
	end = input(msg[1])
	for i in range(int(start),int(end)+1):
		test_range.append(i)
#	print (test_range)	
#	test_range = test_range((int(start)),(int(end)))
	#return (test_range)
#	digit_list = split_number(test_range) #this splits the provided test range data into a list where each li is a list of the digits of each previously whole li
	elemented_list = list(map(elementify_list, test_range))
	cubed_list = list(map(cube_numbers, elemented_list))
	summed_list = list(map(sum_elements, cubed_list))
	armstrong_list = [] #this is where final answers will be stored
	
	for i in test_range:
		if test_range[i] == summed_list[i]:
			armstrong_list.append(i)
		#print ("Not it")
		#print (armstrong_list)

				
#	print ("this is the digit_list", digit_list)
#	print ("this is elemented list", elemented_list)
#	print ("this is cubed list", cubed_list)
#	print ("This is the li I'm trying to sum", summed_list)
	print ("this is armstrong_set", armstrong_list)
	#print ("this is split_cubed_list", split_cubed_list)
	#return (cubed_list)

check_armstrong()

#def list_armstrongs():
#	final_list = []
#	for i in test_range:
#		if check_armstrong() 
		
		
		