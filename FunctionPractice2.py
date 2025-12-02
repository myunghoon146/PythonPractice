# 넘겨받은 리스트의 모든 욧솧의 값을 2배로 증가시키는 함수 구현
# 리턴 X / 원본은 과연 바뀌었을까?

lst = [1,2,3,4,5,4,3,2,1]

def DoubleUpList(lst): #6번 줄의 lst와 8번줄의 lst는 다른 변수!(지역다름)
    # 타입검사
    # 두배 증가
    for i in range(len(lst)):
        lst[i] *= 2
        
DoubleUpList(lst)
print(lst)        


#  그냥 숫자 두배 증가

def DoubleUp(x):
    x*=2
num = 10
DoubleUp(num)
print(num)    




# 리스트는 객체! (여러 값들을 가지고 있음)
# > 주소값을 가지고있음. 함수에 리스트를 넘기면 주소값이 넘어감!
# 함수에서 조작을 하면 원본도 같이 변함 (얕은 복사)

# num 변수는 객체 아님! 그냥 값을 가지고 있음.
# 함수에 num 넘기면 그냥 숫자 10이 넘어감. 원본 변화 없음()
#  프리미티브 타입(Primitive Type) > 리터럴 값 (Literal)

