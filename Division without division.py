from itertools import count, islice

def solution():
	"""divide two integers without using multiplication, division, or mod operator; if overflow, return MAX_INT"""
	
#	try:
	n = 24
	m = 7
	r = list(range(n))
	ans = m
	rem = m
		#short = list
	#	(islice(r, 0, m))
	division_list = []
	while ans < n:
		
			#print (ans)
			#count = 0
		ans += m
		division_list.append(ans)
			#count += 1
	print (division_list)
	digits = str(len(division_list))
	
	remainder = str(division_list.pop())
	
	remainder_list = []
	
#	if remainder != 0:
	n = int(remainder)
	print (n, m, ans, rem)
	while rem < n:
		rem += m
		remainder_list.append(rem)
		print (n, m, ans, rem)
	print (remainder_list)
	
	remainder = str(len(remainder_list))
		
	print (remainder)	
	print (digits + "." + remainder)
	balls = 24/7
	print (balls)
	
			
			
		
	
	#print (short)
	
#	except (overflowError):
#		print ("MAX_INT")
	
solution()
	