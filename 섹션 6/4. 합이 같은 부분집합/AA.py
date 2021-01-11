import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\4. 합이 같은 부분집합')
sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    if L==n:
        if total-sum == sum:
            print("YES")
            sys.exit(0)   # 프로그램 전체를 종료
    else:
        sum+= a[L]
        DFS(L+1, sum)
        sum-= a[L]
        DFS(L+1, sum)


if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0, 0)
    print("NO")
