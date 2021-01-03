import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\3. 뮤직비디오')
sys.stdin = open('in5.txt', 'rt')

def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n,m = map(int, input().split())
Music=list(map(int, input().split()))
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1

print(res)



# my solution
# lt=1
# rt=sum(a)
# shortest=0
# while lt<=rt:
#     mid = (lt+rt)//2
#     tmp=0
#     cnt=0
#     for i in range(n):
#         tmp+=a[i]
#         if tmp>=mid:
#             cnt+=1
#             tmp=a[i]
#     cnt+=1
#     if cnt<m:
#         rt=mid-1
#     elif cnt>m:
#         lt=mid+1
#     else:
#         shortest=mid
#         rt=mid-1
#
# print(shortest)
