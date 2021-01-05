import sys
import os
from collections import deque
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\9. 증가수열 만들기')
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = deque(map(int, input().split()))
cnt=0
end=0
ch=""
while a:
    if a[0]>end and a[-1]>end:
        if a[0]>a[-1]:
            end=a.pop()
            cnt+=1
            ch+="R"
        else:
            end=a.popleft()
            cnt+=1
            ch+="L"
    elif a[0]>end:
        end=a.popleft()
        cnt+=1
        ch+="L"
    elif a[-1]>end:
        end=a.pop()
        cnt+=1
        ch+="R"
    else:
        break

print(cnt)
print(ch)
