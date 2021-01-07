import sys
import os
from collections import deque
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\5. 공주구하기')
sys.stdin = open('input.txt', 'rt')
n,k = map(int, insput().split())

que = deque(range(1,n+1))
i=0
while len(que)!=1:
  i+=1
  if i%3==0:
    que.popleft()
  else:
    x=que.popleft()
    que.append(x)
print(que[0])
