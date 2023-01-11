# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.

# 단, replace() 메서드는 사용하지 마세요.

sen = input('문자열을 입력하세요 > ')
b = ''

for i in sen:
    if i == 'e':continue
    
    else:
        print(i, end='')
