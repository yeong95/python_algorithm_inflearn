import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\4. 마구간 정하기')
sys.stdin = open('input.txt', 'rt')

def Count(dist):
    cnt=1
    tmp=a[0]
    for i in range(1,n):
        if dist <= (a[i] - tmp):
            cnt+=1
            tmp=a[i]
    return cnt

n,m = map(int, input().split())
a = [int(input()) for _ in range(n)]

a.sort()
lt=1
rt=max(a)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=m:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
