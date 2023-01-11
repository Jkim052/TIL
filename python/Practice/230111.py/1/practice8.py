T, N= map(int, input().split())

for i in range(1, T+1):
    print(f'테스트케이스{i} > ', N)

    for j in range(N):
        a, b = map(int, input().split())
        print('출력 > ', a, b)