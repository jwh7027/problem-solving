x = input().strip()
if(x == ""):
    x = 0
    print(x)
else:
    print(x.count(" ") + 1)