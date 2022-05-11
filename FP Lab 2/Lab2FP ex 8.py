l = [0 for i in range(10)]  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
n = int(input("alege numarul: "))

while n>0:
    
    cifra1 = int(n%10)  #scoate ultima cifra
    l[cifra1] += 1      #adauga de cate ori apare cifra respectiva in nr
    n = n/10            #scoate ultima cifra

for i in range(9, 0, -1):       #i parcurge de la 9 la 0
    while l[i]>0:               
        n = n*10 + i            #ia cifra si o adauga in numarul nou
        l[i] -=1                #scoate o data cifra din lista(se repeta daca are mai multe cifre identice)

print(int(n))
