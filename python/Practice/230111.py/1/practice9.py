T, N= map(int, input().split())

for i in range(1, T+1):
    print(f'테스트케이스{i} > ', N)

    for j in range(1, N+1):
        a, b, c= map(int, input().split())
        print(f'출력{j} > ', a, b, c)