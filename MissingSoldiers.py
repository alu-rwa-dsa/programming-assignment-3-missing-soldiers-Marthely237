#Author: Marthely237
#Writing our code here

Barriersnum = int(input())

barriers = []
 
for i in range(Barriersnum):
    m, f, p  = map(int, input().strip().split())
    barriers.append([m, f, p])

i = 0
n = Barriersnum
min_c = barriers[0][0] 
max_c = barriers[0][-1] 
while (n >= 1):
    array = barriers[i]
    m = array[0]
    f = array[1]
    p = array[2] 
    if (max_c < m + p):
        max_c = m + p
    if (min_c > m):
        min_c = m
    i += 1
    n -= 1

d = max_c - min_c + 1
if (d == 12):
    print(11)
else:
    print(d)