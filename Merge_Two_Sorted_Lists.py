import itertools

def merge_two_sorted_lists():
	"""Given two sorted lists such as l1 = [1, 2, 5] and l2 = [1, 3, 4, 5, 7] combine them into one solution_list = [1, 1, 2, 3, 4, 5, 5, 7]"""
	
	l1 = [1 ,2, 5]
	l2 = [1, 3, 4, 5, 7]
	l3 = sorted(l1 + l2)
	print (l3)
	
merge_two_sorted_lists()