import sys

while True:
	line = sys.stdin.readline()
	if not line:
		break

	x = line.strip(" \n\r\t")
	#a= x.split()

	x = int(x)

	if x>-2147483647 and x<0:
		x = x*-1
		print(x)
	else:
		print(x)
