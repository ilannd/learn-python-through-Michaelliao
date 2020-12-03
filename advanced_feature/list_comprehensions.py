print(list(range(1,11)))
print([x*x for x in range (1,11)])
print([x*x for x in range(1,11) if x%2==0])
print([m+n for m in 'ABC'  for n in 'XYZ'])
import os
print([d for d in os.listdir('..')])

print([x if x%2==0 else -x for x in range(1,11)])