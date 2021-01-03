import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 2\9. 주사위 게임')
print(os.getcwd())
sys.stdin = open('input.txt', 'rt')

t = int(input())


res=0
for i in range(t):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int,tmp)
    if a==b and b==c:
        money = 10000+a*1000
    elif a==b or a==c:
        money = 1000+(a*100)
    elif b==c:
        money = 1000+(b*100)
    else:
        money=c*100
    if money > res:
        res = money
print(res)


# my solution
# money = []
# for i in range(t):
#     a = list(map(int, input().split()))
#     if a[0] == a[1] == a[2] :
#         money.append(10000+a[0]*1000)
#     elif a[0] != a[1] != a[2] :
#         money.append(1000+max(a)*100)
#     else : money.append(max(a)*100)
#
# print(max(money))
