import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\10. 스도쿠 검사')
sys.stdin = open('in5.txt', 'rt')

# a = [list(map(int, input().split())) for _ in range(9)]
#
# if check(a):
#     print("YES")
# else:
#     print("NO")



# my solution
input = [list(map(int, input().split())) for _ in range(9)]
breaker=False
# 행, 열 검사
for i in range(9):
    tmp_col=[]
    tmp_row=[]
    for j in range(9):
        if input[i][j] in tmp_row or input[j][i] in tmp_col:
            breaker=True
            break
        tmp_col.append(input[j][i])
        tmp_row.append(input[i][j])
    if breaker==True:
        break


braker2 = False
for i in range(3):
    for j in range(3):
        tmp=[]
        for k in range(3):
            for s in range(3):
                if input[3*i+k][3*j+s] in tmp:
                    braker2=True
                    break
                tmp.append(input[3*i+k][3*j+s])
            if braker2==True:
                break
        if braker2==True:
            break
    if braker2==True:
        break

if breaker or braker2:
    print("NO")
else:
    print("YES")
