import sys
from collections import deque
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\9. 아나그램(구글)')
sys.stdin=open("input.txt", "r")

p=dict()
for x in input():
    if x in p.keys():
        p[x]+=1
    else:
        p[x]=1
for y in input():
    if y in p.keys():
        p[y]-=1
    else:
        p[y]=1

for x in p.values():
    if x!=0:
        print("NO")
        break
else:
    print("YES")
