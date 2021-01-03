import sys
import os
os.chdir(r'C:\Users\CHOYEONGKYU\Desktop\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\6. 격자판 최대합')
print(os.getcwd())
sys.stdin = open('in1.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2

sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest)

# my solution
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# matrix = np.array(matrix)
#
# column_ = np.max(np.sum(matrix,axis=0))
# row_ = np.max(np.sum(matrix, axis=1))
# diag_1=0
# diag_2=0
# for i in range(n):
#     diag_1+= matrix[i,i]
#     diag_2+= matrix[i, n-i-1]
# print(np.max(np.array([column_,row_,diag_1,diag_2])))


f = open("out1.txt", 'r')
data = f.read()
print("")
print(data)
f.close()
