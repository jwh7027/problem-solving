x = int(input())
count = 0
for i in range(1,x+1):
    if (i <100):
        count +=1
    else :
        a = list(map(int,str(i)))
        b = a[2] - a[1]
        c = a[1] - a[0]
        if (b == c):
            count += 1
print(count)