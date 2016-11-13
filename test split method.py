a= 'dany.admin@bukc.edu.pk'
import re
r=re.sub(r'\W+', '.', a)
b=r.split('.')
for i in b:
    print(i)
