def merge_two_sorted_lists():
	"""Given two sorted lists such as l1 = [1, 2, 5] and l2 = [1, 3, 4, 5, 7] combine them into one solution_list = [1, 1, 2, 3, 4, 5, 5, 7]"""
	
	l1 = [1 ,2, 5]
	l2 = [1, 3, 4, 5, 7]
	l3 = sorted(l1 + l2)
	print (l3)
	
merge_two_sorted_lists()


# challenge #2:  complete same task without repetitions in final list

def no_repetitions_merged_list():
	
	l1 = [1 ,2, 5]
	l2 = [1, 3, 4, 5, 7]
	set_l1 = set()           #cannot do set_l1 = {} because that will create emptry dictionary!
	set_l2 = set()
	for i in l1:
		set_l1.add(i)
	for i in l2:
		set_l2.add(i)
	print (set_l1 | set_l2)
	
	# another way of making a set out of a list is as follows.  Same output as before, just cleaner code
	set_l3 = {*l1}
	set_l4 = {*l2}
	print (set_l3 | set_l4)
	
	
no_repetitions_merged_list()