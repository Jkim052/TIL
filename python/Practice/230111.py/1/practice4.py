T = int(input())
    
print('개수 > ', T)

for i in range(1, T+1):
    N = int(input())
    print(f'테스트케이스{i} > ', N)

    for j in range(N):
        a, b = map(int,input().split())
        print('출력 > ', a, b)