number = int(input('정수를 입력하세요 > '))

if number > 100 or number < 0 :
    print('에러')
elif number < 60 :
    print('불합격')
else :
    print('합격')