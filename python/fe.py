a = int(input())
score_list = []
for i in range(a):
    score_list.append(list(map(int, input().split())))

for i in score_list:
    i.pop(0)
    ave = (sum(i))/(len(i))
    cnt = 0
    for j in i:
        if j > ave:
            cnt += 1
    processpoint = cnt/(len(i))*100
    print( "%0.3f%%" % processpoint)
