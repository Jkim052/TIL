import json
from pprint import pprint
# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
a = [] 

for i in movies_list: # movie_list(list)에 있는 요소(I) 하나씩 출력
    b = {} # b딕셔너리를 초기화 안 그러면 b에 데이터가 계속 쌓인다.
    for key, value in i.items(): # I(dict) 있는 key, value 를 하나씩 꺼냄
        if key == 'id' or key == 'title' or key == 'vote_average' or key == 'overview' or key == 'genre_ids': # key 를 비교함 만약 true면
            b[key] = value # b 라는 딕셔너리에 위에 해당하는 key 와 value를 넣어줌
    a.append(b) # 리스트 a 에 딕셔너리 b 를 요소로 추가함
    
pprint(a)