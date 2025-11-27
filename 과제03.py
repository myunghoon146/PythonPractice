### 과제 01| 임의의 정수 5개를 입력받아 오름차순으로 정렬하시오.
numbers=[]
for i in range(5):
    num=int(input(f"{i+1}번째 정수를 입력하시오: "))
    numbers.append(num)
numbers.sort()
print("오름차순 정렬 결과: ", numbers)
    