T = int(input())
for num in range(1, T+1):
        a = []
        a = list(map(int,input().split()))
        ave = sum(a) / len(a)
        print(f'#{num} {round(ave)}')
