a = input()
a = int(a)

if a >= 1 and a <= 4000:
    if a % 4 == 0 and a % 400 == 0 or a % 4 == 0  and a % 100 != 0  :
        print(1)
    else :
        print(0)

