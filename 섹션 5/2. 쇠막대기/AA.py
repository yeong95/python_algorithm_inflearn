import sys
import os
from collections import deque
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\2. 쇠막대기')
sys.stdin = open('in2.txt', 'rt')

a = input()
stack=[]
cnt=0
end='('
for x in a:
    if x=='(':
        stack.append(x)
        end=x
    elif x==')' and end=='(':
        stack.pop()
        cnt+=len(stack)
        end=x
    elif x==')' and end==')':
        stack.pop()
        cnt+=1
        end=x
print(cnt)
