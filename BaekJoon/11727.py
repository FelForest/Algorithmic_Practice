'''
문제
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×17 직사각형을 채운 한가지 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

예제 입력 1 
2
예제 출력 1 
3
예제 입력 2 
8
예제 출력 2 
171
예제 입력 3 
12
예제 출력 3 
2731
'''
# 처음 생각한 것
# 문제 똑바로 읽어
'''
#번호 적어!
# 11727
# 접근 방식 ( Approach )
# dp
# 규칙을 찾으면 됨
import sys
#from heapq import heappop,heappush
#from collections import deque
#sys.setrecursionlimit(10000000)
input = sys.stdin.readline

dp = [0,1]
n = int(input())
for i in range(2,n + 1):
  if i % 2:
    dp.append((dp[i-1] * 2) - 1)
  else:
    dp.append((dp[i-1] * 2) + 1)
print(dp[n]%10007)
'''
# 더 줄일 방법이 없을까 생각했음
# 조건문을 줄일수록 더 적어짐
#번호 적어!
# 11727
# 접근 방식 ( Approach )
# dp
# 규칙을 찾으면 됨
import sys
#from heapq import heappop,heappush
#from collections import deque
#sys.setrecursionlimit(10000000)
input = sys.stdin.readline

dp = [0,1,3]
n = int(input())
for i in range(3,n+1):
  dp.append((dp[i-1] + 2*dp[i-2]) % 10007)
print(dp[n])
