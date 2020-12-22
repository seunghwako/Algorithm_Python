result = []

while True :
    a,b = map(int, input().split())
    if a == b == 0 :
        break
    result.append(a+b)

for r in result :
    print(r)