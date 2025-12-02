#Function2.py
# 입력값은 없는데 반환값은 있는 함수 형태
# 즉 Return이 있다 ~~

# GetPi 구현
import math
print(math.pi)

def GetPi():
    print("파이를 원하는가...주도록 하지..")
    return math.pi


print(GetPi()*3*3)

# 랜던 사용하는 방법
import random # 요놈 먼저 포함시키기
# 랜덤한 정수 뽑아내기
# random.randint(시작, 끝)

# 랜덤값 1~10 10번 출력
for i in range (10):
    print(random.randint(1,10), end= ",  ")
    

# GetRandom10 > 1~10까지 랜덤한 숫자 하나 리턴해줌. 
def GetRandom10():
    return random.randint(1,10)
#GetRandom10을 10번 출력
print()
for i in range(10):
    print(GetRandom10())    
    
    
# GetRandom100 > 1~100 랜덤한 정수 리턴. 이친구 10번 실행 
# GetRandom10To20 > 10~20 랜덤한 정수 리턴. 10번 실행

def GetRandom100():
    return random.randint(1,100)
for i in range(10):
    print(GetRandom100(), end=" ,")
    
def GetRandom10To20():
    return random.randint(10,20)
for i in range(10):
    print(GetRandom10To20(), end=" ,")
    
# 오늘의 야식 메뉴는?
def 오늘뭐먹지():
    lis = ["페페로니 피자", "소보로 치킨", "뿌링클"]
    # 리스트에서 하나 뽑아줘!! -> choice 선택~
    return random.choice(lis)
print("\n오늘의 야식 메뉴! :", 오늘뭐먹지())    
    
            
