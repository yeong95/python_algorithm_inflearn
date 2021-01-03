import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\5. 수들의 합')
print(os.getcwd())
sys.stdin = open('in5.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int,input().split()))
lt=0
rt=1
tot=a[0]
cnt=0

while True:  # 이 방식이 나의 solution보다 훨씬 빠름
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)

# my solution
# n, max = map(int, input().split())
# n_list = list(map(int,input().split()))
# lt=0
# rt=1
# cnt=0
# while rt < n+1:
#     if sum(n_list[lt:rt]) < max:
#         rt+=1
#     elif sum(n_list[lt:rt]) == max:
#         cnt+=1
#         lt+=1
#     elif sum(n_list[lt:rt]) > max:
#         lt+=1
#
# print(cnt)



#
#
# f = open("out5.txt", 'r')
# data = f.read()
# print("")
# print(data)
# f.close()
