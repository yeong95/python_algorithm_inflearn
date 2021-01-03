import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\2. 랜선자르기')
sys.stdin = open('input.txt', 'rt')

def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k,n = map(int, input().split())
Line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest,tmp)

lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)



# my soluiton - wrong answer
# n,m = map(int, input().split())
# a = [int(input()) for _ in range(n)]
# lt=1
# rt=max(a)
# while True:
#     mid = (lt+rt)//2
#     tmp=0
#     for i in range(n):
#         tmp+=a[i]//mid
#     if tmp<m:
#         rt=mid
#     elif tmp>m:
#         lt=mid
#     else:
#         if lt==mid:
#             print(mid)
#             break
#         else:
#             lt=mid
