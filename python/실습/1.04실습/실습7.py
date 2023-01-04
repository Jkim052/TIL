# 양의 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수 중 가장 작은 값을 출력하세요.

# 단, min() 함수는 사용하지 마세요.

number_list =[-1, 40, -245, 9, -100000000]
a=0
for L in number_list:
    if a == 0:
        a = L
    elif a < L:
        a = a
    else :
        a = L

print(a)