# 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.
sen = input("문자열을 입력하세요 > ")

c = {}

for a in sen:
    if a in c:
        c[a] += 1
    else:
        c[a] = 1
c = sorted(c.items())

for key, value in c:
    print(key , value)