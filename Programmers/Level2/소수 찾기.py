from itertools import permutations
def checkPrime(n): #소수 판별
    if n < 2:
        return False
    
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    num = []
    #모든 숫자(순열)
    for i in range(1,len(numbers) + 1):
        num.append(list(permutations(numbers,i)))
    num = [int(''.join(y)) for x in num for y in x]
    #숫자 배열의 길이
    for i in num:
        if checkPrime(i):
            answer.append(i)
    return len(set(answer))