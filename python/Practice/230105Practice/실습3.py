# 입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요.
from datetime import date

dict_variable = {
    "이름": "정우영",
    "생년": "20000101",
    "회사": "하이퍼그로스",
}

### 이하 문제 해결 코드 작성
a=dict_variable["생년"]
b= str(int(str(date.today())[0:4])-int(a[0:4]))

print("나이 : "+ b +"세")
