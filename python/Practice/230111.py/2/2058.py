num = int(input())
s = 0
for i in range(1, 5):
   a = int((num % (10**i)) / 10**(i-1))
   s += a
print(s)