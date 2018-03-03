from itertools import product, permutations, combinations


def threeSum():
	"""given an array of integers S = [-1, 0, 1, 2, -1, 4], find all unique sets of triplets in which a+b+c=0; the solution set must not contain duplicate triplets"""
	
	S = [-1, 0, 1, 2, -1, 4]
		
#	options = list(permutations(S)	
#	options = list(product(S, repeat=3))
	options = list(combinations(S, 3))
	
#	print (options)

	for i in options:
		if sum(i) == 0:
			print (i)
	
	
	
	
threeSum()