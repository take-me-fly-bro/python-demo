def getnum(fileName):
	s = ""
	with open(fileName) as f:
		for char in f.read():
			if char.isdigit():
				s+=char
	return s

print(getnum("/home/shiyanlou/String.txt"))
