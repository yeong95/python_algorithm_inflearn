import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\1. 재귀함수란(이진수출력)')
sys.stdin = open('input.txt', 'rt')

n = int(input())
def make_binary(num):
    if num==0:
        return
    else:
        make_binary(num//2)
        print(num%2, end='')


make_binary(n)
