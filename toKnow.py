# if an exception is catched in "except", the "try" statement continues iterating until the "break" statement or iteration's end
for i in range(10):
	try:
		if 10 / i == 2.0:
			break
	except ZeroDivisionError:
		print(1)
	else:
		print(2)
