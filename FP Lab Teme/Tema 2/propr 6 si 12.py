meniu =  "1 -> Problema 6\n2 -> Problema 12\n3 -> Problema 5\n4 -> iesire"
print(meniu)
try:
 intrebare = int(input("Ce vrei sa faci? "))
    
 if intrebare == 1:
    sir = []
    n = int(input("Introdu numarul de elemente si apoi sirul: "))

    for i in range(0, n):
            elem = int(input())

            sir.append(elem)

    st_best = 0
    dr_best = 0
    
    def gasit(x, v):
        for i in v:
            if(i == x):
                return True

        return False

    for st in range(0, n):
        for dr in range(0, n):
            l = []
            for i in range(st, dr+1):
                if dr_best - st_best < i - st:
                        st_best = st
                        dr_best = i
                if gasit(sir[i] ,l):
                    break
                l.append(sir[i])
                if i == n - 1:
                    if dr_best - st_best <i - st + 1:
                        st_best = st
                        dr_best = i + 1
                    
    print("Lungimea este: ", dr_best  - st_best)
    print("Sirul este: ")
    for i in range(st_best, dr_best):
            print(sir[i])


 elif intrebare == 2:
    sir = []
    n = int(input("Introdu numarul de elemente si apoi sirul: "))
    for i in range(0, n):
        elem = int(input())
        
        sir.append(elem)

    st_best = 0
    dr_best = 0

    for st in range(0, n):
        for dr in range(0, n):
            for i in range(st+1, dr+1):
                if (sir[i]>0 and sir[i-1]<0) or (sir[i]<0 and sir[i-1]>0):
                    if dr_best - st_best < i - st:
                        st_best = st 
                        dr_best = i
                else:
                    break
                        
                

    print("Lungimea este: ", dr_best + 1 - st_best)
    print("Sirul este: ")
    for i in range(st_best, dr_best + 1):
            print(sir[i])

 elif intrebare == 3:

    sir = []
    n = int(input("Introdu numarul de elemente si apoi sirul: "))
    for i in range(0, n):
        elem = int(input())
        
        sir.append(elem)

    st_best = 0
    dr_best = 0

    for st in range(0, n):
        for dr in range(0, n):
            for i in range(st+1, dr+1):
                if (sir[i]==sir[i-1]):
                    if dr_best - st_best < i - st:
                        st_best = st 
                        dr_best = i
                else:
                    break

    print("Lungimea este: ", dr_best + 1 - st_best)
    print("Sirul este: ")
    for i in range(st_best, dr_best + 1):
            print(sir[i])

 elif intrebare == 4:
    print("La revedere!")
                        

 elif intrebare > 4:
    print("Nu ati ales o comanda din meniu! La revedere!")
            
 else: print("La revedere!")

except ValueError:
    print("Nu ati ales o comanda din meniu! La revedere!")










                








