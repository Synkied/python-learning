print("How many cats do you own?")
num_cats = input()
try:
	if int(num_cats) >= 4:
		print("That is a lot of cats.")
	elif int(num_cats) < 0:
		print("Oh, you have negative cats ?")
	else:
		print("That is not that many cats.")
except ValueError:
	print("That is not an integer")