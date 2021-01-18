import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 7\2. 휴가')
# sys.stdin=open("in1.txt", "r")

def DFS(v,sum):
    global res
    # print(path)
    if v>n:
        return
    if sum>res:
        # print(sum)
        res=sum
    for i in range(v,n):
        # path.append(a[i][0])
        DFS(a[i][0]+a[i][1],sum+a[i][2])
        # path.pop()


n=int(input())
a=[]
path=[]
for i in range(n):
    x1,x2 = map(int, input().split())
    a.append((i,x1,x2))
# print(a)

res=0
DFS(0,0)
print(res)
