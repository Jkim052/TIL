# 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수들의 평균을 출력하세요.

# 단, len() / sum() 함수는 사용하지 마세요.
number_list =[7, 2, 3, 4, 5]
a=0
s=0

for i in number_list:
    a+=1
    s+=i 
   
print(s/a)