import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 2\3. k번째 큰 수')
print(os.getcwd())
sys.stdin = open('input.txt', 'rt')
t, k = map(int, input().split())

a = list(map(int, input().split()))
res = set()

for i in range(t):
    for j in range(i+1, t):
        for m in range(j+1, t):
            res.add(a[i] + a[j] + a[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])
