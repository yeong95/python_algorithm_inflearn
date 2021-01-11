import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\5. 바둑이 승차')
#sys.stdin=open("in4.txt", "r")
def DFS(L, sum, tsum):
    global largest
    if sum+(total-tsum)<largest:
        return
    if sum>n:
        return
    if L==m:
        if sum>=largest:
            largest=sum
    else:
        DFS(L+1, sum+a[L], sum+a[L])
        DFS(L+1, sum, sum+a[L])


if __name__=="__main__":
    n,m =map(int, input().split())
    a=[int(input()) for _ in range(m)]
    largest=0
    total=sum(a)
    DFS(0, 0,0)
    print(largest)
