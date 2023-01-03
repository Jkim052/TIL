list_variable = [-1, 3, 5, -2, 1, 9, 21, -3, -5]

for element in list_variable:
    if element < 0:
        continue
    
    print(element, end=" ")
    
"""
-1 -2 -3 -5
"""
# continue 는 이후의 반복문을 수행하지 않음
# 고로
"""
3 5 1 9 21
"""