import sys
import os
from collections import deque
os.chdir(r'/home/yeong95/inflearn_python_algorithom/python_algorithm_inflearn/섹션 7/4. 동전바꿔주기')
# sys.stdin=open("input.txt", "r")

def DFS(L,sum):
    global res
    if sum>tot:
        return
    if sum==tot:
        res+=1
    elif L==n:
        if sum==tot:
            res+=1
    else:
        for i in range(0,num[L]+1):
            DFS(L+1,sum+i*coin[L])
        
res=0
tot=int(input())
n=int(input())
coin=deque()
num=deque()
for _ in range(n):
    x,y=map(int, input().split())
    coin.append(x)
    num.append(y)
DFS(0,0)
print(res)
