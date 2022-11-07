import sys
#from heapq import heappop,heappush
#sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n,m,k = map(int,input().split())
castles = list(map(int,input().split()))
p = list(map(int,input().split()))

broken = []

for i in range(k-1):
  broken.append([p[i],sum(castles[p[i]-1:p[i+1]-1])])

broken.append([p[-1],sum(castles[p[-1]-1::])])
broken.sort(reverse = True, key = lambda x : x[1])
#print(broken)
guard = []
for i in range(m):
  guard.append(broken[i][0])

guard.sort()
print(*guard,sep="\n")
