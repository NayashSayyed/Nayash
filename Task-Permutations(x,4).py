''' task is let x = (0,1,2,3,4,5,6,7,8,9)
and let password  = (5,7,3,8)
it run should (x,4)'''

import itertools as it

x = (0,1,2,3,4,5,6,7,8,9)
c = it.permutations(x,4)
#for i in list(c):
    #print(i)
import time
start = time.time()

for i in list(c):
    if i <= (5,7,3,8):
        print(i)
        if i == (5,7,3,8):
            time.sleep(1)
            print('-Found it-')
            end = time.time()
            print(round(end-start,2))
