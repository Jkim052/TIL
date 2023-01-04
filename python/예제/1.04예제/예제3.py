a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n):
    if number % 2 == 0:
        a = a + 1
        # 0 2 4 6 8 / 5
    if number % 3 == 0:
        b = b + 1
        # 0 3 6 9   / 4
    if number % 4 == 0:
        c = c + 1
        # 0 4 8     / 3
    if number % 5 == 0:
        d = d + 1
        # 0 5       / 2
print(a, b, c, d) # 5 4 3