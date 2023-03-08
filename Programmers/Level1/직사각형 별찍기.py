a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print("*",end="")
    print()

#시간복잡도 O(1) 
answer = ('*'*a +'\n')*b
print(answer)