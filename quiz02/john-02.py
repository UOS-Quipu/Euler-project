
sum = 2
i = 1
j = 2
while i+j < 4000000:
	k = i + j
	if k % 2 == 0 :
		sum += k
	i,j = j,k

print sum
