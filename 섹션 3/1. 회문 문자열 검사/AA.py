import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\1. 회문 문자열 검사')
print(os.getcwd())
sys.stdin = open('in3.txt', 'rt')

T = int(input())


# for i in range(T):
#     s = input()
#     s = s.upper()
#     size = len(s)
#     for j in range(size//2):
#         if s[j]!=s[-1-j]:
#             print("#%d NO" %(i+1))
#             break
#     else: print("#%d YES" %(i+1))
#
# for i in range(n):
#     s = input()
#     s = s.upper()
#     if s == s[::-1]:
#         print("#%d YES" , %(i+1))
#     else :
#         print("#%d NO", %(i+1))

# 2번째 방법이 파이썬스럽지만 1번 방식으로 하는게 좋음


#my solution
for i in range(T):
    a = input().lower()
    tmp = ""
    for k in range(len(a)-1,-1,-1):
        tmp += a[k]
    if tmp == a :
        print("#%d YES" %(i+1) )
    else : print("#%d NO" %(i+1))
