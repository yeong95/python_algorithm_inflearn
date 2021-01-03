import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 2\6. 자릿수의 합')
print(os.getcwd())
sys.stdin = open('input.txt', 'rt')

T = int(input())
Numbers = list(map(int, input().split()))

#1 - 몫과 나머지
def digit_sum(x):
    sum = 0
    while x>0:
        sum += x%10
        x = x//10
    return sum


#2 - str
# def digit_sum(x):
#     sum=0
#     for i in str(x):
#         sum += int(i)
#     return sum

max = -214700000
for x in Numbers:
    tot = digit_sum(x)
    if tot > max :
        max = tot
        res = x

print(res)


# my solution
# def digit_sum(x):
#     x = str(x)
#     tmp = 0
#     for i in range(len(x)):
#         tmp += int(x[i])
#     return tmp
#
# max_digit = 0
# max_index = 0
# for i, number in enumerate(Numbers):
#     if digit_sum(number) > max_digit :
#         max_digit = digit_sum(number)
#         max_index = i
#
# print("%d"  %(Numbers[max_index]))
