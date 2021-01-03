import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 2\5. 정다면체')
print(os.getcwd())
sys.stdin = open('input.txt', 'rt')

a,b = list(map(int, input().split()))
cnt = [0]*(a+b+3)
for i in range(1, a+1):
    for j in range(1, b+1):
        cnt[i+j] += 1
max = 0
for i in range(a+b+1):
    if cnt[i] > max:
        max = cnt[i]
for i in range(a+b+1):
    if cnt[i]==max:
        print(i, end=' ')

# my solution
# tmp = []
# if a < b :
#     for x in range(a,b+1):
#         tmp.append(1+x)
# else :
#     for x in range(b,a+1):
#         tmp.append(1+x)
#
# print(tmp)
