a = []
b = {}
c = 0
with open("data/fruits.txt", "r", encoding= 'UTF8') as f:
    for line in f:
        line = line.replace("\n", '')
        a.append(line)
# 여기서 걍 딕셔너리 형태로 만들었어도 될 듯
for i in a:
    if i[-5:] == 'berry':
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
for i in b:
    c += 1

print(c)

with open("03.txt", "w", encoding= 'UTF8') as f:
    f.write(f'{c}\n')
    for l in b:
        f.write(f"{l}\n")