list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
리스트에 요소가 3개 밖에 없는데 범위에 해당하지 않는 것을 출력하려고 시도 했기에
0 1 2

"""