# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.

# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.

sen = input('문자열을 입력하세요 > ')
index = 0
e = 0

for i in sen:
    if i == 'e':
        e += 1
        print(index)
        break
    index += 1
if e == 0:
    print(-1)