def triangles():
    l=[1]
    while True:
        yield l
        l=[0]+l+[0]
        l=[l[i]+l[i+1] for i in range(len(l)-1)]
n=0
results=[]
for t in triangles():
    results.append(t)
    n=n+1
    if n==10:
        break
print(results)