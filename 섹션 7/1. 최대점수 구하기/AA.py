import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 7\1. 최대점수 구하기')
#sys.stdin=open("in1.txt", "r")

# def DFS(L, time, score):
#     global res
#     if time>m:
#         return
#     if L==n:
#         if score>res:
#             res=score
#     else:
#         DFS(L+1,time,score)
#         DFS(L+1,time+a[L][1], score+a[L][0])

def DFS(s, score, time):
    global res
    if time>m :
        return
    if score>res:
        res=score
    for i in range(s, n):
        DFS(i+1,score+aa[i][0],time+aa[i][1])


n, m=map(int, input().split())
aa=[]
for i in range(n):
    x1,x2 = map(int, input().split())
    aa.append((x1,x2))


res=0
DFS(0,0,0)
print(res)
