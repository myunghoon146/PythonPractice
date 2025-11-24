total = 0
while True:
    num = int(input("정수를 입력하세요: "))
    
    if num<0:
        break
    
    total+=num
    
    print("누적 합:", total)