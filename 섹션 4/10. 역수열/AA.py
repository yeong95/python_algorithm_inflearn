import sys
import os
from collections import deque
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\10. 역수열')
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(map(int , input().split()))
tmp=[0]*n
cnt=0
for i,x in enumerate(a):
    for ii,y in enumerate(tmp):
        if y==0:
            cnt+=1
        if cnt==x+1:
            tmp[ii]=i+1
            cnt=0
            break
for x in tmp:
    print(x, end=' ')
