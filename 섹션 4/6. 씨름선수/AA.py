import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\6. 씨름선수')
sys.stdin = open('input.txt', 'rt')

n = int(input())
info=[]
for _ in range(n):
    a,b = map(int, input().split())
    info.append((a,b))
info.sort(reverse=True)
largest=0
cnt=0
for height, weight in info:
    if weight > largest:
        largest=weight
        cnt+=1
print(cnt)
