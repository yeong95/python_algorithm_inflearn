import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\1. 이분검색')
sys.stdin = open('input.txt', 'rt')

n,m = map(int, input().split())
a=list(map(int, input().split()))
a.sort()
lt=0
rt=n-1

while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1

# my solution 
# while True:
#     mid = (lt+rt)//2
#     if a[mid] < m:
#         lt=mid+1
#     elif a[mid] > m:
#         rt=mid-1
#     else:
#         break
# print(mid+1)
