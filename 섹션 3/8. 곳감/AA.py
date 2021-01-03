import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\8. 곳감')
print(os.getcwd())
sys.stdin = open('in1.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

s=0
e=n-1
res=0
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i < n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)




# # my solution
# for _ in range(m):
#     row, direction, m = map(int, input().split())
#     tmp = a[row-1].copy()
#     if direction == 0:
#          for i in range(n):
#              a[row-1][i-m] = tmp[i]
#     else:
#         for i in range(n):
#             if i+m>4:
#                 a[row-1][i+m-5] = tmp[i]
#             else :
#                 a[row-1][i+m] = tmp[i]
# print(a)

f = open("out1.txt", 'r')
data = f.read()
print("")
print(data)
f.close()
