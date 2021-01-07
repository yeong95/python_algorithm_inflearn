import sys
import os
from collections import deque
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\4. 후위식 연산')
sys.stdin = open('input.txt', 'rt')
a = input()

stack=[]
for x in a:
  if x.isdecimal():
    stack.append(int(x))
  else:
      x2=stack.pop()
      x1=stack.pop()
      if x=='+':
        stack.append(x1+x2)
      elif x=='-':
        stack.append(x1-x2)
      elif x=='*':
        stack.append(x1*x2)
      elif x=='/':
        stack.append(x1/x2)

print(stack[0])
