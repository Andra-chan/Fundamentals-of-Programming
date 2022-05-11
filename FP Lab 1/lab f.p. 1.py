l = [1, 2, 3, 4,5]

for e in l:
    e = e**2
    print(e)

for i in range(10,0,-1): # range(0,5) -> 0,1,2,3,4
    print(i)

while len (l) > 0:
    a = l.pop()
    if a <3:
        a = a**2
    elif a < 5:
        a=0-a
    else:
        a=0
    print(a)

print("Gata")
    
