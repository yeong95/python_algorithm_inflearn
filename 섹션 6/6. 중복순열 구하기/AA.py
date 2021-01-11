import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\6. 중복순열 구하기')
sys.stdin=open("input.txt", "r")

def DFS(L):
    global a
    if L==m:
        for x in a:
            print(x, end=' ')
        print()
        return
    else:
        for i in range(n):
            a[L]=i+1
            DFS(L+1)


if __name__=="__main__":
    n,m =map(int, input().split())
    a=[0]*m
    DFS(0)
    print(n**m)
