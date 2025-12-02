# Function3.py
# 입력만 있고, 반환은 없는 형태
# 매개변수가 존재하고, Return은 없음.

# 숫자 하나 넘겨주면 그 숫자 두배 출력해주기 
# DoublePrint 
x = 10

def DoublePrint(gk):
    print("두배가돼!!: ", gk*2)
    
DoublePrint(x)   

# 숫자 두개 받아서 더한 후 출력 > PrintTwo 

x=15
y=12

def PrintTwo(kl,mw):
    print(kl+mw)

PrintTwo(x,y)

# PrintTwo 매가변수가 2개! -> 1개만 넘겨주면 어케될까?


#  이름 잘 짓는 법.
# 카멜 스타일(케이스)
# koreaItAcademy 첫 글자 소문자. 새로운 단어?대문자 시작
# 변수명
# 파스칼 스타일(케이스)
# KoreaItAcademy 카멜이랑 같은데 맨 앞도 대문자
# 함수, 클래스, 메소드

# 스네이크 스타일(케이스)
# korea_it_academy 다 소문자 + 새로운단어 나오면 _ 밑줄


# 안씀, 굳이 쓴다면? > 파일 & 폴더명 

# 중요한 순서 > 점점 디테일
# 가급적 동사 또는 명사형 단어 사용하기 


# 그리고 타자 연습 꼭하기

# PrintEvenOdd
# 숫자 하나 입력받아서, 짝수면 짝수, 홀수면 홀수를 출력하기

import random
def PrintEvenOdd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
        
for i in range(10):
    x = random.randint(1,100)
    PrintEvenOdd(x)            