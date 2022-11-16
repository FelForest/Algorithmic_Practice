'''
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1 
3
7
8
9
'''

# 문제좀 잘 읽어라!
'''
#번호 적어!
# 2667
# 접근 방식 ( Approach )
# 걍 탐색
# 이미 한번 비슷한 문제를 푼적있어서 접근은 맞는거 같음
# 조건을 함수 내에서 잘못 작성하여서 인덱스에러가 뜸
# 함수 들어오기전에 확있했어야 했음
import sys
#from heapq import heappop,heappush
#from collections import deque
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def search(x,y):
  global count
  dx = [-1,0,0,1]
  dy = [0,1,-1,0]
  field[x][y] = 0
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    if 0 <= nx < n and 0 <= ny < n and field[nx][ny]:
      count += 1
      search(nx,ny)
      
global count
n = int(input())
a = [list(map(str,input().split())) for _ in range(n)]
field = [[int(j) for j in a[i][0]] for i in range(n)]
result = []
for i in range(n):
  for j in range(n):
    count = 1
    if field[i][j]:
      search(i,j)
      result.append(count)
print(len(result),*result,sep="\n")
'''

#번호 적어!
# 2667
# 접근 방식 ( Approach )
# 걍 탐색
# 이미 한번 비슷한 문제를 푼적있어서 접근은 맞는거 같음
# 조건을 함수 내에서 잘못 작성하여서 인덱스에러가 뜸
# 함수 들어오기전에 확있했어야 했음
import sys
#from heapq import heappop,heappush
#from collections import deque
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def search(x,y):
  global count
  dx = [-1,0,0,1]
  dy = [0,1,-1,0]
  field[x][y] = 0
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    if 0 <= nx < n and 0 <= ny < n and field[nx][ny]:
      count += 1
      search(nx,ny)
      
global count
n = int(input())
a = [list(map(str,input().split())) for _ in range(n)]
field = [[int(j) for j in a[i][0]] for i in range(n)]
result = []
for i in range(n):
  for j in range(n):
    count = 1
    if field[i][j]:
      search(i,j)
      result.append(count)
result.sort()
print(len(result),*result,sep="\n")
