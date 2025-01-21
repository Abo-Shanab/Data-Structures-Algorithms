def counter():
    n=1
    while True:
        n*=2
        yield n


l=[]
tmp=1
for i in counter():
    l.append(i)
    if tmp == 9:
        break
    tmp+=1



print(l)