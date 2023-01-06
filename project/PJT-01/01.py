with open("01.txt", "w", encoding= 'UTF8') as f:
    f.write('Hello, Python!\n')
    for l in range(2,7):
        f.write(f'{l-1}일차 파이썬 공부 중\n')

with open("01.txt", "r", encoding= 'UTF8') as f:
    print(f.readlines())