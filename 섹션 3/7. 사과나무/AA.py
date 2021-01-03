import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\7. 사과나무')
print(os.getcwd())
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2

for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)

#my solution
# for k, x in enumerate(a):
#     if k<n//2:
#         for i in range(s,e+1):
#             res+=x[i]
#         s-=1
#         e+=1
#     else :
#         for i in range(s,e+1):
#             res+=x[i]
#         s+=1
#         e-=1
# print(res)


# f = open("out1.txt", 'r')
# data = f.read()
# print("")
# print(data)
# f.close()
