# 양의 정수를 입력받고, 자리수의 합을 출력하세요.

# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.

# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.
a = int(input('양의 정수를 입력하세요 > '))
b = 1
c = 0

while a / (10**(b-1)) >= 1:
    if a <= 0:
        print(-1)
    else:
        c += (a % (10 ** b) - a % (10 ** (b - 1)))/(10**(b-1))
        b += 1


print(int(c))