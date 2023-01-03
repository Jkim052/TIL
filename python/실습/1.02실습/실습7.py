import statistics

number1 = int(input('첫 번째 숫자를 입력해주세요 > '))
number2 = int(input('두 번째 숫자를 입력해주세요 > '))
number3 = int(input('세 번째 숫자를 입력해주세요 > '))

avg = [number1, number2, number3]

print(statistics.mean(avg))