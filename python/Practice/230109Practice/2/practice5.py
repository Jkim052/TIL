# 양의 정수 3개를 입력받고, 3개의 양수를 - 로 연결해서 출력하세요.

# 단, join() 메서드는 사용하지마세요.

phone = list(map(int, input('문자열을 입력하세요 > ').split()))
cnt = 1
for i in phone:
    if len(phone) == cnt:
        print(i)
    else:
        print(i, end='-')
    cnt += 1