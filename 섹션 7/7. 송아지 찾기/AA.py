import sys
import os
from collections import deque
os.chdir(r'/home/yeong95/inflearn_python_algorithom/python_algorithm_inflearn/섹션 7/7. 송아지 찾기')
sys.stdin=open("input.txt", "r")

start,end=map(int,input().split())
max=10000
ch=[0]*(max+1)
dis=[0]*(max+1)
ch[start]=1
dis[start]=0
dq=deque()
dq.append(start)
while dq:
    now=dq.popleft()
    if now==end:
        break
    for next in(now-1,now+1,now+5):
        if 0<next<=max:
            if ch[next]==0:
                dq.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[end])

    
