import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\5. 회의실 배정')
sys.stdin = open('input.txt', 'rt')

n = int(input())
time=[]
for _ in range(n):
    a,b = map(int, input().split())
    time.append((a,b))
sorted_time=sorted(time, key=lambda x:(x[1],x[0]))
cnt=1
tmp=sorted_time[0]
for i in range(1,n):
    if tmp[1] <= sorted_time[i][0]:
        cnt+=1
        tmp=sorted_time[i]
print(cnt)
