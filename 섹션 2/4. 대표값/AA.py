import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 2\4. 대표값')
print(os.getcwd())
sys.stdin = open('input.txt', 'rt')

T = int(input())

Numbers = list(map(int, input().split()))

average = round(sum(Numbers) / T)

min = np.float('inf')
for idx, x in enumerate(Numbers):
    tmp = abs(x - average)
    if tmp < min :
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1
print(average, res)

# my solution
# diff = np.array(Numbers) - average
# min_number = min(abs(diff))
# ans_index = 0
# if min_number in diff :
#     ans_index = np.where(diff == min_number)[0][0] + 1
# else : ans_index = np.where(diff == -min_number)[0][0] + 1
# print("%d %d" %(average, ans_index))
