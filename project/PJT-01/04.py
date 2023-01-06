a = {}

with open("data/fruits.txt", "r", encoding= 'UTF8') as f:
    for line in f:
        line = line.replace("\n", '')
        if line in a:
            a[line] += 1
        else:
            a[line] = 1

for key, value in a.items():
    print(f"{key} {value}")
    
with open("04.txt", "w", encoding= 'UTF8') as f:
    for key, value in a.items():
        f.write(f"{key} {value}\n")

