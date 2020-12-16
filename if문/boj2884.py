h, m  = input().split()
h = int(h)
m = int(m)

if h == 0 and m < 45 :
    h = 23
    m = m + 15
else :
    if m < 45 :
        h = h - 1
        m = m + 15
    else :
        m = m - 45   

print(h, m , end = '')
