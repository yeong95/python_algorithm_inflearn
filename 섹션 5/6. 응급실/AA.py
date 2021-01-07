import sys
import os
from collections import deque
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\6. 응급실')
#sys.stdin = open('input.txt', 'rt')
n,k = map(int, input().split())
a = list(map(int,input().split()))
a = deque(a)

cnt=0
while True:
    x=a.popleft()
    for y in a:
        if x<y:
            a.append(x)
            if k==0:
                k=len(a)-1
            else:
                k-=1
            break
    else:
        cnt+=1
        if k==0:
            break
        else:
            k-=1

print(cnt)
