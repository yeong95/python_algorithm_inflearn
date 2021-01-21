import sys
import os
from collections import deque
os.chdir(r'/home/yeong95/inflearn_python_algorithom/python_algorithm_inflearn/섹션 7/6. 알파코드')
sys.stdin=open("input.txt", "r")


def DFS(L):
    global cnt
    if L==len(a):
        for x in res:
            print(chr(x+64),end='')
        print()
        cnt+=1
    else:
        for i in range(1,27):
            if i<10:
                if i==int(a[L]):
                    res.append(i)
                    DFS(L+1)
                    res.pop()
            else:
                if i==int(a[L:L+2]):
                    res.append(i)
                    DFS(L+2)
                    res.pop()
                    
a=input()
cnt=0
res=[]
DFS(0)
print(cnt)