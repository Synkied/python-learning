# l = [1,2,2,3]

# def factorial(n):
# 	"""Calculates the number of permutations of n items (n: integer >= 0)"""
# 	y = 1 # if x < 2, return 1
# 	for i in range(2,n+1): # if x >= 2...
# 		y*=i # calculate factorial of x. eg (x = 3 -> i in range(2,4) -> y = 1*2 -> y = 2. y = 2*3 -> y = 6. factorial of 3 is 6.)
# 	return y

# print(factorial(6))

# def count_repetitions(a_list):
# 	repeted = []
# 	uniq = []
# 	for item in a_list:
# 		if item not in uniq: # if item is not in the uniq list, then we count the number of times it is in the origin list a_list. This assures we don't count n times the item is present //
# 		# eg. [1,1,1] would return 3 3 3 if we didn't count only items appended to uniq
# 			uniq.append(item) # append the item to the uniq list
# 			counting = a_list.count(item) # and count the number of times the item is present in the origin list l
# 			if counting > 1: # if item is repeted more than once
# 				repeted.append(counting) # append counting to the repeted list, to get the number of times each item is repeted
# 	return repeted


# def permutation(x,y):
# 	if type(y) == list: # y can be a list of number of times of repeted items.
# 	# if y is such a list, we can determine how many unique permutations there are, ignoring y repeted nums
# 	# the calculation goes : factorial(x)//fact(y[0])*fact(y[1])....*fact(y[n]))

# 		m = factorial(x)
# 		for j in y:
# 			n = 1
# 			for i in range(2,j+1):
# 				m//=n*i #  (eg. factorial(8)//(factorial(2)*factorial(3)) = 3360)
# 		return m

# 	if x == 1:
# 		return 1
# 	else:
# 		z = factorial(x)//factorial(x-y)
# 		return z

# def combination(x,y):
# 	if x == 1:
# 		return 1
# 	else:
# 		z = factorial(x)//(factorial(x-y)*factorial(y))
# 		return z


# def permutlist(seq, er=False):
# 	"""
# 	Returns lists of permutations in seq
# 	if er = True, eliminates repeted elements
# 	"""
# 	p = [seq] # p = matrix of seq
# 	n = len(seq)

# 	for k in range(0,n-1):
# 		for i in range(0,len(p)):
# 			z = p[i][:] # p[i][:] is equivalent to list(p[i]). Creates a copy of p[i] in z
# 			for c in range(0,n-k-1):
# 				z.append(z.pop(k))

# 				if er==False or z not in p:
# 					p.append(z[:]) # copies the z list inside p, to get all permutations (with repeted elements in seq)
# 	print("Number of permutations:",len(p))
# 	return sorted(p)

# print(permutation(10,4))
# print(permutation(len(l),count_repetitions(l))) # permutations of UNIQUE items in a list, via count_repetitions
# print(combination(n,k))

# print(permutlist(l))
