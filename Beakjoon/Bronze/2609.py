num1,num2 = input().split()
num1 = int(num1)
num2 = int(num2)
greatest_common_divisor = 1
#최대공약수
for i in range(2,min(num1,num2)+1):
    if(num1 % i == 0 and num2 % i == 0):
            greatest_common_divisor = i

#최소공배수
a = num1 // greatest_common_divisor
b = num2 // greatest_common_divisor

print(greatest_common_divisor)
print(greatest_common_divisor*a*b)