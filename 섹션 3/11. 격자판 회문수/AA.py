import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\11. 격자판 회문수')
sys.stdin = open('input.txt', 'rt')

board = [list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt+=1
print(cnt)

# my solution
# a = [list(map(int, input().split())) for _ in range(7)]
# cnt=0
# for i in range(7):
#     s=0
#     e=4
#     for _ in range(3):
#         if a[i][s] == a[i][e] and a[i][s+1] == a[i][e-1]:
#             cnt+=1
#         if a[s][i] == a[e][i] and a[s+1][i] == a[e-1][i]:
#             cnt+=1
#         s+=1
#         e+=1
#
# print(cnt)
