# 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.

# 단, count() 메서드는 사용하지마세요.

sen = input('문자열을 입력하세요 > ')
c = 0
for i in sen:
     if i == 'e':
        c+=1
print(c)