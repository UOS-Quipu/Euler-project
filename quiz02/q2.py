result = 2
f3n = 2
f3n2 = 8
f3n3 = 0
while f3n2 <= 4000000:
  result = result + f3n2
  f3n3 = f3n + 4 * f3n2
  f3n = f3n2
  f3n2 = f3n3
print(result)
