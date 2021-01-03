import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\2. 숫자만 추출')
print(os.getcwd())
sys.stdin = open('input.txt', 'rt')

# f = open("out3.txt", 'r')
# data = f.read()
# print(data)
# f.close()

T = (input())

res=0
for x in T:
    if x.isdecimal():
        res=res*10+int(x)
print(res)
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)
# my solution
# tmp=""
# for x in T:
#     try:
#         int(x)
#         tmp += x
#     except :
#         pass
# number = int(tmp)
# a=0
# for x in range(1, number+1):
#     if number % x == 0:
#         a += 1
#
# print(number)
# print(a)
