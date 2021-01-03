import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 2\8. 뒤집은 소수')
print(os.getcwd())
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10 + t
        x = x//10
    return res

def isPrime(x):
    if x == 1 : return False
    for i in range(2, x//2+1):
        if x%i==0: return False  # reuturn makes def over
    else :  return True


for x in a :
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')

# my solution
# def reverse(x):
#     tmp = str(0)
#     for i in range(len(str(x))-1, -1,-1):
#         tmp += str(x)[i]
#     return int(tmp)
#
# def isPrime(x):
#     ch = [0] * (x+1)
#     for i in range(2,x):
#         for j in range(i, x+1, i):
#             ch[j] = 1
#     if ch[x] == 0 :
#          tmp = True
#     else : tmp = False
#     if x == 1 : tmp = False
#     return tmp
#
# Numbers = list(map(int, input().split()))
#
# for x in Numbers:
#     if isPrime(reverse(x)) : print(reverse(x), end= ' ')
