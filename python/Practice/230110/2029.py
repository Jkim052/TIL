# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.
T = int(input())
for num in range(1, T+1):
        a = []
        a = list(map(int,input().split()))
        ave = sum(a)/len(a)
        print(f'#{num} {ave}')