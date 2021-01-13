import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\11. 수들의 조합')
sys.stdin=open("input.txt", "r")
def DFS(L, s, sum):
    global cnt
    if L==m and sum%div==0:
        cnt+=1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])


n, m=map(int, input().split())
a=list(map(int, input().split()))
div = int(input())
res=[0]*(n+1)
cnt=0
DFS(0, 0, 0)
print(cnt)
