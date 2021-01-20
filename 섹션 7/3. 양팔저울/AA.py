import sys
import os
os.chdir(r'/home/yeong95/inflearn_python_algorithom/python_algorithm_inflearn/섹션 7/3. 양팔저울')
sys.stdin=open("in5.txt", "r")

def DFS(L,sum):
    global res
    if L==n:
        if 0<sum:
            res.add(sum)
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum-a[L])
        DFS(L+1,sum)


res=set()
n = int(input())
a = list(map(int, input().split()))
DFS(0,0)
# print(res)
print(sum(a)-len(res))
