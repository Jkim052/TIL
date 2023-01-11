# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.
string = input('문자열을 입력하세요 > ').split()
dic = {}

for i in string:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for key, value in dic.items():
    print(key, value)