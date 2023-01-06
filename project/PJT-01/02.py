a = []
with open("data/fruits.txt", "r", encoding= 'UTF8') as f:
    print(type(f))
    for line in f:
        a.append(line)

b = len(a)
with open("02.txt", "w", encoding= 'UTF8') as f:
    f.write(f"{b}")
