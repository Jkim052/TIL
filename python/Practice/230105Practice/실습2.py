# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.

# 알파벳 모음 : a(A) e(E) i(I) o(O) u(U)

# 단, count() 메서드는 사용하지마세요.
sen = input("문자열을 입력하세요 > ")
c = 0

for a in sen:
        if a == ("a" or  'A' or  "e" or  'E' or  "i" or  'I' or  "o" or  'O' or  'u' or  'U'):
                c += 1
print(c)