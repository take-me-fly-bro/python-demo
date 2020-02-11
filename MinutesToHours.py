import sys

# transfer function
def Hours(min):
	min = int(min)
	if min < 0:
		raise ValueError
	else:
		print(int(min/60),"H",min%60,"M")

# user argument
userInput = sys.argv[1]

# call function
try:
	Hours(userInput)
except:
	print("Parameter Error")