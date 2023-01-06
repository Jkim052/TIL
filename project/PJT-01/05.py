import json
from pprint import pprint
# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
a = {}

for key, value in movie.items():
    if key == 'id' or key == 'title' or key == 'vote_average' or key == 'overview' or key == 'genre_ids':
        a[key] = value
    else: continue
pprint(a)

