result = 0
for x in range (100, 1000):
  for y in range (100, 1000):
    z = x * y
    b = str(z)
    a = b[::-1]
    if b == a:
        if z > result:
            result = z
print(result)
