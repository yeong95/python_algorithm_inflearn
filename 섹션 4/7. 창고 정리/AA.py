import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\7. 창고 정리')
sys.stdin = open('input.txt', 'rt')

n = int(input())
b = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    max_idx = b.index(max(b))
    min_idx = b.index(min(b))
    b[max_idx] -=1
    b[min_idx] +=1
print(max(b)-min(b))
