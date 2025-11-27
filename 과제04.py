### 2. 다음 리스트에서 문자열의 길이가 5 이상인 단어만 뽑아 새로운 리스트로 만드세요.
words = ["apple", "dog", "banana", "cat", "orange", "egg"] 
result = [word for word in words if len(word) >= 5]
print(result)