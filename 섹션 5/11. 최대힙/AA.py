import sys
import heapq as hq
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\11. 최대힙')
sys.stdin=open("input.txt", "r")
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a)) # root node를 pop
    else:
        hq.heappush(a,-n)
