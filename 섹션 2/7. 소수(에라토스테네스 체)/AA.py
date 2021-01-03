import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 2\7. 소수(에라토스테네스 체)')
print(os.getcwd())
sys.stdin = open('in2.txt', 'rt')

n = int(input())

ch = [0] * (n+1)
cnt = 0

for i in range(2,n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)
