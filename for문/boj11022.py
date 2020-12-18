n = input()
n = int(n)
result = []


for i in range(1, n+1) : 
    a,b = map(int, input().split())
    if a > 0  and a < 10 and b > 0 and b < 10 :
        result.append("Case #" + str(i) + ": " + str(a) + " + " + str(b) + " = " + str(a+b))

for r in result :
    print(r)