import sys
import os
os.chdir(r'/content/python_algorithm_inflearn/섹션 6/15. 경로탐색')
sys.stdin=open("in3.txt", "r")

n,m = map(int, input().split())
gp=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    gp[a-1][b-1]=1

# for i in range(n):
#     for j in range(n):
#         print(gp[i][j], end=' ')
#     print()

def DFS(L):
  global cnt
  if res[L]==n or L==n:
    print(res)
    cnt+=1
  else: 
    for i,x in enumerate(gp[res[L]-1]):
      if x==1 and tmp[i]==0:
        res.append(i+1)
        tmp[i]=1
        DFS(L+1)
        res.pop()
        tmp[i]=0
cnt=0
res=[1]
tmp=[0]*n
tmp[0]=1        
DFS(0)
print(cnt)