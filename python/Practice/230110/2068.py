T = int(input())
for num in range(1, T+1):
        a = []
        a = list(map(int,input().split()))
        
        print(f'#{num} {max(a)}')