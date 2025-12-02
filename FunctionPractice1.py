# FunctionPractice1.py > 함수 실습 1
# 넘겨받은 숫자만큼 0의 개수가 들어 있는 리스트를 리턴하는 함수 구현
# MakeList1(size)

def MakeList1(size):
    lst = []
    for i in range(size):
        lst.append(0)
    return lst

testList = MakeList1(10)
print(type(testList))
print(testList)

# 1부터 넘겨받은 숫자까지 순서대로 데이터가
# 들어있는 리스트를 리턴하는 함수 구현

def MakeList2(size):
    lst=[]
    for i in range(1,size+1):
        lst.append(i)
    return lst    

testList = MakeList2(10)
print(testList)

# 숫자 두개를 넘겨받아 첫 숫자부터 두번째
# 숫자까지 순서대로 데이터가 들어있는
# 리스트를 만든 후, 총 합계를 출력 후 리스트를 리턴




# PrintListReserve(lst)
# 넘겨받은 리스트에 대해 모든 요소를 공백으로 구분해서
# 역순으로 출력하는 함수 구현

def PrintListReserve(lst): 
    for i in range( len(lst)-1,-1, -1):
        # 길이 -1부터 -1전까지(0까지) 1씩 감소
         print(lst[i], end="  ")
    print()
    

        