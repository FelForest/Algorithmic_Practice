'''
문제
해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?

입력
첫째 줄에 테스트 케이스가 주어진다. 테스트 케이스는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)이 주어진다.
다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.
모든 문자열은 1이상 20이하의 알파벳 소문자로 이루어져있으며 같은 이름을 가진 의상은 존재하지 않는다.

출력
각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력하시오.

예제 입력 1 
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
예제 출력 1 
5
3
'''

'''
#번호 적어!
# 9375
# 접근 방식 ( Approach )
# 조합
# 
import sys
#from heapq import heappop,heappush
#from collections import deque
#sys.setrecursionlimit(10000000)
from itertools import product
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
  wears = {}
  c = []
  m = int(input())
  for i in range(m):
    a,b = map(str,input().split())
    if b in wears:
      wears[b].append(a)
    else:
      wears[b] = [a]
  for i in wears:
    c.append(wears[i])
  if len(c) > 1:
    t = 0
    for i in c:
      t += len(i)
    result.append(t + len(list(product(*c))))
  else:
    result.append(len(list(product(*c))))
print(*result,sep="\n")
'''
# 솔직히 어디서 틀린것인지 모르겠음
# 검색했더니 위 방법보다 더 좋은 방법을 사용하는거 같아서 가져옴

#번호 적어!
# 9375
# 접근 방식 ( Approach )
# 조합
# 
import sys
#from heapq import heappop,heappush
#from collections import deque
#sys.setrecursionlimit(10000000)
input = sys.stdin.readline

for _ in range(int(input())):
  wears = {}
  for i in range(int(input())):
    a,b, = map(str,input().split())
    if b in wears:
      wears[b] += 1
    else:
      # 안입는 경우도 생각
      wears[b] = 2
  c = 1
  for v in wears.values():
    c *= v
  # 다 안입는 경우를 뺀것
  print(c - 1)
  
