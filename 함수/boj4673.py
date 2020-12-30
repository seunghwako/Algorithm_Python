def d(n) :
    result = n
    for i in str(n) :
        result += int(i)
    return result

number = []

for j in range(1,10000) :
   self_number = d(j)

   if self_number < 10000 :
       number.append(self_number)
   if j not in number :
       print(j) 
