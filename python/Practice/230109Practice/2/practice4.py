# 문자열과 알파벳을 공백으로 구분해서 입력받고, 문자열에서 입력한 알파벳의 개수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.

sen , a = input('문자열을 입력하세요 > ').split()
cnt = 0

for i in sen:
    if i == a:
        cnt += 1
print(cnt)