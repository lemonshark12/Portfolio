from itertools import count, islice

n = 24
m = 7

def solution():
	"""divide two integers without using multiplication, division, or mod operator; if overflow, return MAX_INT"""
	digits_and_remainder = calculate_digits(n, m)
	print (digits_and_remainder)
	calculate_remainder(digits_and_remainder)

def calculate_digits(n, m):
	
	r = list(range(n))
	ans = m
	rem = m
	division_list = []
	while ans < n:
		ans += m
		division_list.append(ans)
#	print (division_list)
	digits = len(division_list)
	last = division_list[-1]
	remainder = (n - digits*m)*10
	return (digits, remainder)
	
def calculate_remainder(digits_and_remainder):
	remainders_list = []
	remainder_list = []
	digits, rem = int(digits_and_remainder[0]), digits_and_remainder[1]
#	print (digits, rem)
#	digits = 3, rem = 30
	
	remainder = m
#	remainder = 7
	while rem != 0:
		while remainder < rem:
#	while 7 < 30
			remainder += m
# 	add 7 to the remainder variable
			remainder_list.append(remainder)
#	attach the remainder variable to the remainder_list
#		print (n, m, remainder, rem)
			print (remainder_list)
	
		remainders = len(remainder_list)
		last = remainder_list[-1]
		rem = (rem - remainders*m)*10
		decimals = remainders_list.append(remainders)
		remainder_list = []

	print (last)
	print (remainder)
	print (decimals)
	#print (new_remainder)
	
	#while remainders != 0:
	
	#	print (decimals)
				
	#return (remainders)	
	
	
	
#	print (str(digits) + "." + str(remainders_list.join()))
	balls = 24/7
	print (balls)
	
			
			
		
	
	#print (short)
	
#	except (overflowError):
#		print ("MAX_INT")
	
solution()
	