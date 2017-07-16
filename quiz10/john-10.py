
sosus = [2,3,5]

def isSosu(num) :
	for s in sosus :
		if s == 2 or s == 3 :
			continue
		if s*s > num :
			return True
		if num%s == 0 :
			return False
	return True

i = 1

limit = 2000000
while True :
	a = 6*i + 1
	b = 6*i + 5

	if a > limit :
		break
	if isSosu(a) :
		sosus.append(a)
	if b > limit :
		break
	if isSosu(b) :
		sosus.append(b)
	
	i += 1

'''print sosus'''
print sum(sosus)

