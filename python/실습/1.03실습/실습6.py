sentence = input('문자열을 입력하세요 > ')

for i in range(-1 , -(len(sentence)+1), -1) :
    print(sentence[i])