# -*- coding:utf8 -*-
import time

def get_submul(num):
	submul = {}

	d = 2
	while num != 1:
		c = 0
		
		while num % d == 0:
			num = int(num / d)
			c += 1

		if c != 0:
			submul[d] = c

		d += 1

	r = 1
	for i in submul.values():
		r *= i + 1

	return r

if __name__ == "__main__":
	start = time.time()
	# content

	index = 1
	cached = 1

	while True:
		total = cached
		cached = get_submul( index + 1 if index % 2 == 0 else int((index + 1) / 2))
		total *= cached

		if total >= 500:
			print(index * (index + 1) / 2)
			break

		index += 1

	end = time.time()
	print(end - start)