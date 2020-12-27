n = int(input())
score = list(map(int, input().split()))

max = max(score)

result =  0

for s in score :
    result += (s / max) * 100

print(result / n)
    



