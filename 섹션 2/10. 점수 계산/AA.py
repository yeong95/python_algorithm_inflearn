import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 2\10. 점수 계산')
print(os.getcwd())
sys.stdin = open('input.txt', 'rt')

t = int(input())

a = list(map(int, input().split()))

sum = 0
cnt = 0
for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0
print(sum)


# my solution
# fn_score = 0
# tmp = 0
# for i, x in enumerate(a) :
#     if x == 0 :
#         tmp = 0
#         continue
#     if x == 1 and x == a[i-1]:
#         tmp += 1
#         fn_score += tmp
#     elif x == 1 and x != a[i-1]:
#         tmp = 1
#         fn_score += tmp
#
# print(fn_score)
