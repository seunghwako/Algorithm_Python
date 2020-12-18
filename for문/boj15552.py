import sys
t = sys.stdin.readline().rstrip()
t = int(t)
result = []
for i in range(0, t) :
    a,b = map(int, sys.stdin.readline().split())
    result.append(a+b)
for r in result :
    print(r)
