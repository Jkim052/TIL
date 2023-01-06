import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
# movie 에 있는 genre_ids 를 genre_names 로 교체하라

genre_names = []

for i in genres_list: # genre_list 안에 있는 dict(i)을 하나하나 꺼내본다
    if i['id'] in movie['genre_ids']: # 만약 i['id'] 의 값이 movie['genre_ids'] 안에 있는 값과 일치한다면
        genre_names.append(i['name']) # genre_names 에 key(name), value(genre) 를 추가한다.

movie['genre_names'] = genre_names
movie.pop('genre_ids')

pprint(movie)