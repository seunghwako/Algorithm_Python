t = input()
t = int(t)
result = []

for i in range(0, t) :
    a,b = input().split()
    a = int(a)
    b = int(b)
    result.append(a+b) # 결과를 저장하기 위해 result list에 append(추가)

for r in result :
    print(r)

