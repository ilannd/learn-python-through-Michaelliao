d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
print('\n')
for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for k ,v in d.items():
    print(k+":"+str(v))
for  i,value in enumerate(['A','B','C']):
    print(i,value)
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)

from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))



