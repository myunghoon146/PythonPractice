grades={ 
    'Alice':[85,90,92],
    'Bob':[78,81,85],
    'Charlie':[92,95,77]            
}

averages={name:sum(scores)/len(scores) for name,scores in grades.items()}
for name,avg in averages.items():
    print(f"{name}의 평균 점수: {avg:.2f}")