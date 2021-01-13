import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\14. 인접행렬')
sys.stdin=open("input.txt", "r")

n,m = map(int, input().split())
gp=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int, input().split())
    gp[a-1][b-1]=c

for i in range(n):
    for j in range(n):
        print(gp[i][j], end=' ')
    print()

#
# a=[[1,2,3],[4,5,6],[7,8,9]]
# a[0][1] = 100
# print(a)
