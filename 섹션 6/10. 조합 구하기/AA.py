import sys
import os
os.chdir('/content/python_algorithm_inflearn/섹션 6/10. 조합 구하기')
sys.stdin=open("in5.txt", "r")
def DFS(L):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if res[L-1]<i:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0

if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*n
    ch=[0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)
