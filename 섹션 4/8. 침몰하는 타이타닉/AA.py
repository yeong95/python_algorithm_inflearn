import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\8. 침몰하는 타이타닉')
sys.stdin = open('input.txt', 'rt')

n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
cnt=0
while a!=[]:
    pop = a.pop(0)
    tmp=len(a)
    for i in range(len(a)):
        if pop+a[i] <= m:
            cnt+=1
            del a[i]
            break
    if len(a) == tmp:
        cnt+=1

print(cnt)
