dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # 위 조건문의 조건식이 무엇을 의미하는지 작성하세요.
    # dict_variable 에 '거주지'란 key 가 없으면 
    # '거주지 : 서울특별시' 란 키와 값을 추가하시오
    
print(dict_variable) 
# 이름 정우영
# 생년월일 19000101
# 회사 하이퍼그로스
# 거주지 서울특별시 X

# {'이름' : '정우영', '생년월일' : '19000101', '회사' : '하이퍼그로스', '거주지' : '서울특별시'}