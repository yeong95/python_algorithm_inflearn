import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 7\2. 휴가')
sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    global res
    print(path)
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1:
            path.append(L+T[L])
            DFS(L+T[L], sum+P[L])
            path.pop()
        path.append(L+1)
        DFS(L+1, sum)
        path.pop()

if __name__=="__main__":
    path=[]
    n=int(input())
    T=list()
    P=list()
    for i in range(n):
        a, b=map(int, input().split())
        T.append(a)
        P.append(b)
    res=-2147000000
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)
    print(res)
