import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\7. 동전교환')
sys.stdin=open("input.txt", "r")

def DFS(L,sum):
    global res
    if sum>m or L>res:
        return
    if sum==m :
        res=L
        return
    else:
        for i in range(n):
            DFS(L+1, sum+coin[i])


if __name__=="__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    coin.sort(reverse=True)
    m = int(input())
    res=2147000000
    DFS(0,0)
    print(res)
