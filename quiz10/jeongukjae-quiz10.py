# -*- coding: utf8 -*-

import time

start = time.time()

list_of_num = list(range(2, 2000001))

for num in list_of_num:
	if num is not None:
		for i in range(num<<1, 2000001, num):
			list_of_num[i - 2] = None

print(sum(list(filter(None.__ne__, list_of_num))))
print(time.time() - start)
