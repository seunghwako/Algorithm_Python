n = int(input())

for i in range(n) :
    s = input()
    score = 0
    count = 0

    for j in s :
        if j == 'O' :
            count += 1
        elif j == 'X' :
            count = 0
        score += count
    print(score)





    

