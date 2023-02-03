word = input().lower()
ls = []

for i in range(97,123): #아스키코드 a~z범위
    if chr(i) in word: #숫자를 아스키코드 문자열 변환 
        a = word.index(chr(i))
        ls.append(a)
    else:
        ls.append(-1)

for i in ls:
    print(i, end= " ")