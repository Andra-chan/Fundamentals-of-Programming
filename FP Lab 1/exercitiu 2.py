a=int(input("Introduceti numarul: "))
m=1
for d in range(2,a):
    if(a%d)==0:
        m=0
if(m==1): print ("Numarul este prim")
else: print ("Numarul nu este prim")
