# 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.

# 두 값이 같으면 False를 출력하세요

number1 = int(input('첫 번째 정수를 입력해주세요 > '))
number2 = int(input('두 번째 정수를 입력해주세요 > '))

if number1 == number2 :
    print('False')

elif number1 > number2 :
    for i in range(number1-1, number2, -1) :
        print(i, end=" ") 

else :
    for i in range(number2-1, number1, -1) :
        print(i, end=" ") 