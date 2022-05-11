l1 = [0 for i in range(10)]
l2 = [0 for i in range(10)]
n1 = int(input("alege numarul: "))
n2 = int(input("alege numarul: "))
while n1>0:
    cifra1 = int(n1%10)
    l1[cifra1] = 1
    n1 = n1/10
while n2>0:
    cifra2 = int(n2%10)
    l2[cifra2] = 1
    n2= n2/10
a = True
for i in range(0,10):
    if(l1[i]!=l2[i]):
        a = False
if a == True:
    print("au proprietatea")
else:
    print ("nu au proprietatea")

