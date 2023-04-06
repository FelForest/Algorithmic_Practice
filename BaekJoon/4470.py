# 암만 재활 치료라고는 하지만 너무한거 아닌가 싶다.
# 실버 4 2개 못풀어서 이거 푼다.
N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append(s)

for n in range(N):
    print(str(n+1)+".",S[n])
