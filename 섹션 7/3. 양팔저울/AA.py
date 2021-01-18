import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 7\3. 양팔저울')
sys.stdin=open("in5.txt", "r")

def DFS(L,sum):
    global res
    if L==n:
        if 0<sum:
            res.add(sum)
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum-a[L])
        DFS(L+1,sum)


res=set()
n = int(input())
a = list(map(int, input().split()))
DFS(0,0)
# print(res)
print(sum(a)-len(res))
