a = input()
b = input()
a = int(a)
b = int(b)

if a >= -1000 and a <= 1000 and a != 0  and b >= -1000 and b <= 1000 and b != 0 :
    if a > 0 and b > 0 :
        print(1)
    elif a < 0 and b > 0 :
        print(2)
    elif a < 0 and b < 0 :
        print(3)
    else :
        print(4)