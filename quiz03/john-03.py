
def divide(num):
	for i in xrange(2,num/2) :
		if(num%i == 0) :
			return i, num/i
	return -1, num

def soinsu(num) :
	insu = []
	if num < 2 :
		return num

	current = divide(num)
	'''print current'''
	while current[0] != -1 :
		insu.append(current[0])
		current = divide(current[1])
		print current
	insu.append(current[1])

	return insu

print soinsu(600851475143)

