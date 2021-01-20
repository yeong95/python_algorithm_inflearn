import sys
import os
from collections import deque
os.chdir(r'/home/yeong95/inflearn_python_algorithom/python_algorithm_inflearn/섹션 7/5. 동전분배하기')
sys.stdin=open("input.txt", "r")

def DFS(L,x1,x2,x3):
    global res
    if L==n:
        # print(x1,x2,x3)
        # print(max(x1,x2,x3)-min(x1,x2,x3))
        if len(set((x1,x2,x3)))==3 and max(x1,x2,x3)-min(x1,x2,x3)<res:
            res=max(x1,x2,x3)-min(x1,x2,x3)
    else:
        DFS(L+1,x1+a[L],x2,x3)
        DFS(L+1,x1,x2+a[L],x3)
        DFS(L+1,x1,x2,x3+a[L])

res=21600000
n=int(input())
a=[int(input()) for _ in range(n)]
a1=a2=a3=0
DFS(0,a1,a2,a3)
print(res)
