import sys
from collections import deque
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\8. 단어찾기')
sys.stdin=open("input.txt", "r")

n = int(input())
word = dict()
for i in range(n):
    word[input()]=i

for _ in range(n-1):
    x=input()
    if x in word.keys():
        del word[x]
print(list(word.keys())[0])
