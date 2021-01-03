import sys
import os
import numpy as np
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\4. 두 리스트 합치기')
print(os.getcwd())
sys.stdin = open('in3.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 시간복잡도 - n
p1=p2=0
c=[]
while p1<n and p2<m:   # 둘 중 하나의 포인터가 끝까지 가면 종료
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]

for x in c:
    print(x, end=' ')



# my solution - 이런식으로 풀면 안된다.... 시간복잡도 nlog(n)
# tmp=[]
# for i in range(1,5):
#     a = list(map(int,input().split()))
#     if i%2 == 0:
#         tmp += a
# tmp.sort()
# print(tmp)





f = open("out3.txt", 'r')
data = f.read()
print("")
print(data)
f.close()
