#!/home/wizard/anaconda3/bin/python3.7

from time import time

N = 5000

values = []
t = time()
for v in range(1, N):
    for s in range(v,N):
        values.append( divmod(v,s))
print('for loop:{:.4f}'.format(time() - t ))

t = time()
values2 = [  divmod(v,s) for v in range(1,N) for s in range(v,N)]
print('for expr:{:.4f}'.format(time() - t ))

t = time()

values3 = list(
   (  divmod(v,s) for v in range(1,N) for s in range(v,N) ) 
)
print('gen expr:{:.4f}'.format(time() - t ))