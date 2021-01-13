import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\8. 순열 구하기')
sys.stdin=open("in2.txt", "r")

def DFS(L):
    global cnt
    if L==m:
        for x in a:
            print(x, end=' ')
        cnt+=1
        print()
        return
    else:
        for i in range(n):
            if tmp[i]==0:
                a[L]=i+1
                tmp[i]+=1
                DFS(L+1)
                tmp[i]-=1

if __name__=="__main__":
    n,m =map(int, input().split())
    a=[0]*m
    tmp=[0]*n
    cnt=0
    DFS(0)
    print(cnt)
