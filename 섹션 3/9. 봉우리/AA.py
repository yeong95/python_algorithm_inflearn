import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\9. 봉우리')
#sys.stdin = open('in5.txt', 'rt')
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)

cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):  # all은 모든 조건을 만족해야 true
            cnt+=1
print(cnt)

# my solution
# for i in range(len(a)):
#     a[i].insert(0,0)
#     a[i].append(0)
#
# cnt=0
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         if a[x][y] > a[x][y-1] and a[x][y] > a[x][y+1] and a[x][y]>a[x-1][y] and a[x][y]>a[x+1][y]:
#             cnt+=1
# print(cnt)




# f = open("out5.txt", 'r')
# data = f.read()
# print("")
# print(data)
# f.close()
