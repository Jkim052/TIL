# 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.

# 두 값이 같으면 False를 출력하세요

number1 = int(input('첫 번째 정수를 입력해주세요 > '))
number2 = int(input('두 번째 정수를 입력해주세요 > '))

if number1 == number2 :
    print('False')

elif number1 > number2 :
    for i in range(number2+1, number1) :
        print(i, end=" ") 

else :
    for i in range(number1+1, number2) :
        print(i, end=" ")

# 문지수님 풀이 min 함수, max 함수 배워가기
#
# a = int(input("첫 번째 정수를 입력하세요 > "))
# b = int(input("두 번째 정수를 입력하세요 > "))

# for i in range(min(a,b)+1, max(a,b)):
#     print(i)
# if a == b:
#     print("False")

# 이 풀이가 훨씬 간단한거 같다.


# 노현석님 풀이 변수 치환하는 법 배워가기

# num1 = int(input('첫 번째 정수를 입력하세요 > '))
# num2 = int(input('두 번째 정수를 입력하세요 > '))


# max = num1
# if(max < num2):
#     max = num2
#     min = num1
# else:
#     min = num2

# if num1 == num2:
#     print(False)
# else:
#     for i in range(min+1, max):
#         print(i)