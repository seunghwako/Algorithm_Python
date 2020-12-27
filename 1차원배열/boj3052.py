final = []

for i in range(10) :
    a = int(input())
    result = a % 42
    
    if result not in final :
        final.append(result)

print(len(final))
        


