n = 10

for element in range(n, -n, -1):
    print(element, end=" ")
    if n < 0: # << 이게 element가 되어야 
        break
"""
10 9 8 8 7 6 5 4 3 2 1 0 -1
"""
# n 이 10 이고 
#     if n < 0:    <<<
#        break  이부분 함정이다.

'''

'''