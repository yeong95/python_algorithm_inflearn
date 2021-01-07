import sys
import os
from collections import deque
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\3. 후위표기식 만들기')
sys.stdin = open('input.txt', 'rt')
a = input()
stack=[]
res=''
for x in a:
  if x.isdecimal():
    res+=x
  else:
    if x=='(':
      stack.append(x)
    elif x=='*' or x=='/':
      while stack and (stack[-1]=='*' or stack[-1]=='/'):
        res+=stack.pop()
      stack.append(x)
    elif x=='+' or x=='-':
      while stack and stack[-1]!='(':
        res+=stack.pop()
      stack.append(x)
    elif x==')':
      while stack and stack[-1]!='(':
        res+=stack.pop()
      stack.pop() #'(' 삭제
while stack:
  res+=stack.pop()
print(res)
