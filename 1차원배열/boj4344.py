case = int(input())

for i in range (case) :
    score = list(map(int, input().split()))
    avg = sum(score[1: ]) / score[0]
    count = 0

    for scr in score[1: ] :
        if scr > avg :
            count += 1
    
    print("%.3f"  %((count/score[0])*100) + "%")
    


