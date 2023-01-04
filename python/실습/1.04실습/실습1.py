# 정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.

# 단, abs() 함수는 사용하지 마세요
#방법1
a = int(input())

if a==0:
    print(a)
elif a>0:
    print(a)
else:
    print(a*-1)

#방법2
a = (a**2)**(1/2)

print(int(a))