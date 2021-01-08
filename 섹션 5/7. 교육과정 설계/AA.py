import sys
from collections import deque
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\7. 교육과정 설계')
sys.stdin=open("in2.txt", "r")

need = input() # 순서
n = int(input())
for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
        if len(dq)==0:
            print("#%d YES" %(i+1))
            break
    else:
        print("#%d NO" %(i+1))
