import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\9. 수열 추측하기')
sys.stdin=open("input.txt", "r")

import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def DFS(L):
    global cnt,res
    if L==n:
        res=[x1*x2 for x1,x2 in zip(a,comb)]
        if sum(res)==m:
            for x in a:
                print(x, end=' ')
            sys.exit(0)
    else:
        for i in range(n):
            if tmp[i]==0:
                a[L]=i+1
                tmp[i]+=1
                DFS(L+1)
                tmp[i]-=1

if __name__=="__main__":
    n,m =map(int, input().split())
    a=[0]*n
    tmp=[0]*n
    comb=[0]*n
    for i in range(len(comb)):
        comb[i]=nCr(n-1,i)
    res=0
    DFS(0)
