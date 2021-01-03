import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\3. 카드 역배치')
print(os.getcwd())
sys.stdin = open('input.txt', 'rt')

a = list(range(21))  # 구간 설정 이렇게 하는게 헷갈리지 않음
for _ in range(10):
    s,e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')


#solution
# card = list(range(1,21))
# for x in range(10):
#     a, b = map(int, input().split())
#     card[a-1:b]=card[a-1:b][::-1]
#
# for x in card:
#     print(x, end=' ')
#
#
# f = open("out5.txt", 'r')
# data = f.read()
# print("")
# print(data)
# f.close()
