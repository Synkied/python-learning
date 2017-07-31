import time as t
from os import path

def createFile(dest):
	"""
	The script creates a text file at the passed in location,
	names file based on date
	"""
	date = t.localtime(t.time())
	print(date)

	## FileName = Day_Month_Year
	name = "%d_%d_%d.txt"%(date[2], date[1], (date[0] %100))
	print (name)

if __name__ == "__main__":
	createFile("Test")
	input("done!")