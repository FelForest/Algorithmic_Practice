'''
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

예제 입력 1 
2
예제 출력 1 
2
예제 입력 2 
9
예제 출력 2 
55
'''
# O(n)보다 더 적은 방법이 있을까?

#번호 적어!
# 11726
import sys
#from heapq import heappop,heappush
#from collections import deque
#sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
dp = [0,1,2]
for i in range(3,n+1):
  dp.append(dp[i-1]+dp[i-2])
print(dp[n]%10007)
