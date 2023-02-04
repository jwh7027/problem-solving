word = input()
count = 0
cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in cro:
    if i in word:
        word = word.replace(i,'0')
print(len(word))