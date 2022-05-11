"""listele ce contin informatiile din pachetele de calatorie: zi/luna/an - inceput/sfarsit, destinatie, pret"""

lista_data_inceput_zi = []
lista_data_inceput_luna = []
lista_data_inceput_an = []
lista_data_sfarsit_zi = []
lista_data_sfarsit_luna = []
lista_data_sfarsit_an = []
lista_destinatie = []
lista_pret = []

"""lista de liste"""

toate_listele = []
toate_listele.append(lista_data_inceput_zi)
toate_listele.append(lista_data_inceput_luna)
toate_listele.append(lista_data_inceput_an)
toate_listele.append(lista_data_sfarsit_zi)
toate_listele.append(lista_data_sfarsit_luna)
toate_listele.append(lista_data_sfarsit_an)
toate_listele.append(lista_destinatie)
toate_listele.append(lista_pret)



""" Pachet de calatorie = data de inceput si cea de sfarsit, destinatia, pretul"""

print("""
Un pachet de calatorie contine:
Data de inceput si cea de sfarsit, destinatia si pretul.
      """)

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

""" Meniul principal cu toate comenzile"""

def meniu1():
    print("""
    1. Pentru a accesa meniul Adaugare, inserati adauga.
    2. Pentru a accesa meniul Stergere, inserati sterge.
    3. Pentru a accesa meniul Cautare, inserati cauta.
    4. Pentru a accesa meniul Rapoarte, inserati raport.
    5. Pentru a accesa meniul Filtrare, inserati filtru.
    6. Pentru a accesa meniul Undo, inserati undo.
    7. Pentru a iesi din program, inserati exit.
    """)
meniu1()

"""Sub-meniuri pentru fiecare meniu"""

def meniu_adaugare():
    print("""
    Meniul Adaugare contine:
    1. Adauga pachet de calatorie.
    2. Modifica pachet de calatorie.
    """)

def meniu_stergere():
    print("""
    Meniul Stergere contine:
    1. Ștergerea tuturor pachetelor de călătorie disponibile pentru o
    destinație dată.
    2. Ștergerea tuturor pachetelor de călătorie care au o durată mai scurtă
    decât un număr de zile dat.
    3. Ștergerea tuturor pachetelor de călătorie care au prețul mai mare
    decât o sumă dată.
    """)

def meniu_cautare():
    print("""
    Meniul Cautare contine:
    1. Tipărirea pachetelor de călătorie care presupun un sejur într-un
    interval dat.
    2. Tipărirea pachetelor de călătorie cu o destinație dată și cu preț mai
    mic decât o sumă dată.
    3. Tipărirea pachetelor de călătorie cu o anumită dată de sfârșit.
    """)
    
def meniu_rapoarte():
    print("""
    Meniul Rapoarte contine:
    1. Tipărirea numărului de oferte pentru o destinație dată.
    2. Tipărirea tuturor pachetelor disponibile într-o anumită perioadă citită
    de la tastatură în ordinea crescătoare a prețului.
    3. Tipărirea mediei de preț pentru o destinație dată.
    """)

def meniu_filtrare():
    print("""
    Meniul Filtrare contine:
    1. Eliminarea ofertelor care au un preț mai mare decât cel dat și o
    destinație diferită de cea citită de la tastatură.
    2. Eliminarea ofertelor în care sejurul presupune zile dintr-o anumită
    lună
.
    """)

def meniu_undo():
    print("""
    Meniul Undo contine:
    1. Refacerea ultimei operații (lista de oferte revine la ce exista înainte
    de ultima operație care a modificat lista).
    """)

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

"""Functiile care formeaza listele cu pachete.(din meniul Adauga, sub-meniul 1)
Fiecare lista contine o informatie din pachet: zi/luna/data-inceput, zi/luna/data-sfarsit, destinatie, pret."""

def lista_adauga_zi_inceput():

    try:
        elem_lista_zi = int(input("\nCe zi doresti sa adaugi la data de inceput? " ))   
        lista_data_inceput_zi.append(elem_lista_zi)
        print("\nAti adaugat la pachetul de calatorie ziua: ", elem_lista_zi)
        print("Zilele de inceput introduse sunt: ", lista_data_inceput_zi)
    except ValueError:
        print("\nNu ati introdus un numar! Va rugam sa reincercati...")
        lista_adauga_zi_inceput()
    
def lista_adauga_luna_inceput():

    try:
        elem_lista_luna = int(input("\nCe luna doresti sa adaugi la data de inceput? " ))   
        lista_data_inceput_luna.append(elem_lista_luna)
        print("\nAti adaugat la pachetul de calatorie luna: ", elem_lista_luna)
        print("Lunile de inceput introduse sunt: ", lista_data_inceput_luna)
    except ValueError:
        print("\nNu ati introdus un numar! Va rugam sa reincercati...")
        lista_adauga_luna_inceput()
        
def lista_adauga_an_inceput():

    try:
        elem_lista_an = int(input("\nCe an doresti sa adaugi la data de inceput? " ))   
        lista_data_inceput_an.append(elem_lista_an)
        print("\nAti adaugat la pachetul de calatorie anul: ", elem_lista_an)
        print("Anii de inceput introdusi sunt: ", lista_data_inceput_an)
    except ValueError:
        print("\nNu ati introdus un numar! Va rugam sa reincercati...")
        lista_adauga_an_inceput()
        
def lista_adauga_zi_sfarsit():

    try:
        elem_lista_zi = int(input("\nCe zi doresti sa adaugi la data de sfarsit? " ))   
        lista_data_sfarsit_zi.append(elem_lista_zi)
        print("\nAti adaugat la pachetul de calatorie zi: ", elem_lista_zi)
        print("Zilele de sfarsit introdusi sunt: ", lista_data_sfarsit_zi)
    except ValueError:
        print("\nNu ati introdus un numar! Va rugam sa reincercati...")
        lista_adauga_zi_sfarsit()
    
def lista_adauga_luna_sfarsit():

    try:
        elem_lista_luna = int(input("\nCe luna doresti sa adaugi la data de sfarsit? " ))   
        lista_data_sfarsit_luna.append(elem_lista_luna)
        print("\nAti adaugat la pachetul de calatorie luna: ", elem_lista_luna)
        print("Lunile de sfarsit introduse sunt: ", lista_data_sfarsit_luna)
    except ValueError:
        print("\nNu ati introdus un numar! Va rugam sa reincercati...")
        lista_adauga_luna_sfarsit()

def lista_adauga_an_sfarsit():

    try:
        elem_lista_an = int(input("\nCe an doresti sa adaugi la data de sfarsit? " ))   
        lista_data_sfarsit_an.append(elem_lista_an)
        print("\nAti adaugat la pachetul de calatorie an: ", elem_lista_an)
        print("Anii de sfarsit introdusi sunt: ", lista_data_sfarsit_an)
    except ValueError:
        print("\nNu ati introdus un numar! Va rugam sa reincercati...")
        lista_adauga_an_sfarsit()
        
def lista_adauga_destinatie():

    try:
        elem_lista_destinatie = str(input("\nCe destinatie doresti sa adaugi? " ))   
        lista_destinatie.append(elem_lista_destinatie)
        print("\nAti adaugat la pachetul de calatorie destinatia: ", elem_lista_destinatie)
        print("Destinatiile introduse sunt: ", lista_destinatie)
    except ValueError:
        print("\nNu ati introdus un numar! Va rugam sa reincercati...")
        lista_destinatie()
        
def lista_adauga_pret():

    try:
        elem_lista_pret = int(input("\nCe preturi doresti sa adaugi? " ))   
        lista_pret.append(elem_lista_pret)
        print("\nAti adaugat la pachetul de calatorie pretul: ", elem_lista_pret, "ron")
        print("Preturile introduse sunt: ", lista_pret)
    except ValueError:
        print("\nNu ati introdus un numar! Va rugam sa reincercati...")
        lista_pret()

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

"""Functiile care modifica listele initiale."""

def modificare_zi_inceput():

    print("Zilele de inceput actuale din pachete sunt: ", lista_data_inceput_zi)
    which_zi_inceput = int(input("\nCe zi de inceput din lista vrei sa modifici? "))  
    modif_zi_inceput = int(input("Cu ce vrei sa modifici data? "))
    for i in range(0, len(lista_data_inceput_zi)):
        if which_zi_inceput == lista_data_inceput_zi[i]:
            lista_data_inceput_zi[i] = modif_zi_inceput
            break

def modificare_luna_inceput():

    print("Lunile de inceput actuale din pachete sunt: ", lista_data_inceput_luna)
    which_luna_inceput = int(input("\nCe luna de inceput din lista vrei sa modifici? "))  
    modif_luna_inceput = int(input("Cu ce vrei sa modifici data? "))
    for i in range(0, len(lista_data_inceput_luna)):
        if which_luna_inceput == lista_data_inceput_luna[i]:
            lista_data_inceput_luna[i] = modif_luna_inceput
            break
    
def modificare_an_inceput():

    print("Anii de inceput actuali din pachete sunt: ", lista_data_inceput_an)
    which_an_inceput = int(input("\nCe an de inceput din lista vrei sa modifici? "))  
    modif_an_inceput = int(input("Cu ce vrei sa modifici data? "))
    for i in range(0, len(lista_data_inceput_an)):
        if which_an_inceput == lista_data_inceput_an[i]:
            lista_data_inceput_an[i] = modif_an_inceput
            break
            
def modificare_zi_sfarsit():

    print("Zilele de sfarsit actuale din pachete sunt: ", lista_data_sfarsit_zi)
    which_zi_sfarsit = int(input("\nCe zi de sfarsit din lista vrei sa modifici? "))  
    modif_zi_sfarsit = int(input("Cu ce vrei sa modifici data? "))
    for i in range(0, len(lista_data_sfarsit_zi)):
        if which_zi_sfarsit == lista_data_sfarsit_zi[i]:
            lista_data_sfarsit_zi[i] = modif_zi_sfarsit
            break

def modificare_luna_sfarsit():

    print("Lunile de sfarsit actuale din pachete sunt: ", lista_data_sfarsit_luna)
    which_luna_sfarsit = int(input("\nCe luna de sfarsit din lista vrei sa modifici? "))  
    modif_luna_sfarsit = int(input("Cu ce vrei sa modifici data? "))
    for i in range(0, len(lista_data_sfarsit_luna)):
        if which_luna_sfarsit == lista_data_sfarsit_luna[i]:
            lista_data_sfarsit_luna[i] = modif_luna_sfarsit
            break

def modificare_an_sfarsit():

    print("Anii de sfarsit actuali din pachete sunt: ", lista_data_sfarsit_an)
    which_an_sfarsit = int(input("\nCe an de sfarsit din lista vrei sa modifici? "))  
    modif_an_sfarsit = int(input("Cu ce vrei sa modifici data? "))
    for i in range(0, len(lista_data_sfarsit_an)):
        if which_an_sfarsit == lista_data_sfarsit_an[i]:
            lista_data_sfarsit_an[i] = modif_an_sfarsit
            break

def modificare_destinatie():

    print("Destinatiile actuale din pachete sunt: ", lista_destinatie)
    which_destinatie = input("\nCe destinatie din lista vrei sa modifici? ")  
    modif_destinatie = input("Cu ce vrei sa modifici destinatia? ")
    for i in range(0, len(lista_destinatie)):
        if which_destinatie == lista_destinatie[i]:
            lista_destinatie[i] = modif_destinatie
            break

def modificare_pret():

    print("Preturile actuale din pachete sunt: ", lista_pret, "ron")
    which_pret = int(input("\nCe pret din lista vrei sa modifici?(ron) "))  
    modif_pret = int(input("Cu ce vrei sa modifici pretul? "))
    for i in range(0, len(lista_pret)):
        if which_pret == lista_pret[i]:
            lista_pret[i] = modif_pret
            break     

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

"""Functiile care fac stergerile cerute"""

def stergere1():

    try:
        print("Destinatiile valabile sunt: ", lista_destinatie)
        stergere1_destinatie = input("Alegeti destinatia: ")
        for i in range(0, len(lista_destinatie)):
            if stergere1_destinatie == lista_destinatie[i]:
                for j in range(0,8):
                    del toate_listele[j][i]
                print("Stergerea a fost realizata cu succes!")
                print("""\nPachetele actualizate sunt: """, toate_listele)
                break
    except ValueError:
        print("\nNu ati introdus un numar! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()
    except IndexError:
        print("\nVa rugam introduceti mai intai un pachet pentru a putea sterge!")
        meniu1()
        meniu_aplicatii()

'def stergere2():'

def stergere3():
    
    try:
        print("Preturile valabile sunt: ", lista_pret)
        stergere3_pret = input("Alegeti pretul: ")
        for i in range(0, len(lista_destinatie)):
            if lista_destinatie[i] > stergere3_pret:
                for j in range(0,8):
                    del toate_listele[j][i]
                print("Stergerea a fost realizata cu succes!")
                print("\nPachetele actualizate sunt: ", toate_listele)
                break
    except ValueError:
        print("\nNu ati introdus un numar! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()
    except IndexError:
        print("\nVa rugam introduceti mai intai un pachet pentru a putea sterge!")
        meniu1()
        meniu_aplicatii()
    

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

"""Functiile care fac cautarile cerute"""

def cautare1():
    try:
        print("Zilele de inceput sunt: ", lista_data_inceput_zi)
        print("Lunile de inceput sunt: ", lista_data_inceput_luna)
        print("Anii de inceput sunt: ", lista_data_inceput_an)
        print("Zilele de sfarsit sunt: ", lista_data_sfarsit_zi)
        print("Lunile de sfarsit sunt: ", lista_data_sfarsit_luna)
        print("Anii de sfarsit sunt: ", lista_data_sfarsit_an)
        tiparire_zi_inceput = int(input("Alegeti ziua de inceput: "))
        tiparire_luna_inceput = int(input("Alegeti luna de inceput: "))
        tiparire_an_inceput = int(input("Alegeti anul de inceput: "))
        tiparire_zi_sfarsit = int(input("Alegeti ziua de sfarsit: "))
        tiparire_luna_sfarsit = int(input("Alegeti luna de sfarsit: "))
        tiparire_an_sfarsit = int(input("Alegeti anul de sfarsit: "))
        for i in range(0, len(lista_data_sfarsit_zi)):
            if tiparire_zi_sfarsit >= lista_data_sfarsit_zi[i] and tiparire_luna_sfarsit >= lista_data_sfarsit_luna[i] and tiparire_an_sfarsit >= lista_data_sfarsit_an[i] and tiparire_zi_inceput <= lista_data_inceput_zi[i] and tiparire_luna_inceput <= lista_data_inceput_luna[i] and tiparire_an_inceput <= lista_data_inceput_an[i]:
                print("""\nPachetele cu cerintele selectate sunt: """
                      "\n1. Ziua de inceput: ", toate_listele[0][i],
                      "\n2. Luna de inceput: ", toate_listele[1][i],
                      "\n3. Anul de inceput: ", toate_listele[2][i],
                      "\n4. Ziua de sfarsit: ", toate_listele[3][i],
                      "\n5. Luna de sfarsit: ", toate_listele[4][i],
                      "\n6. Anul de sfarsit: ", toate_listele[5][i],
                      "\n7. Destinatia: ", toate_listele[6][i],
                      "\n8. Pretul: ", toate_listele[7][i])               
    except ValueError:
        print("\nNu ati introdus un numar! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()
        

def cautare2():

    try:
        print("Destinatiile valabile sunt: ", lista_destinatie)
        print("Preturile valabile sunt: ", lista_pret)
        tiparire_destinatie = input("Alegeti destinatia: ")
        tiparire_pret = int(input("Alegeti pretul: "))
        for i in range(0, len(lista_pret)):
            if tiparire_destinatie == lista_destinatie[i] and tiparire_pret >= lista_pret[i]:
                print("""\nPachetele cu cerintele selectate sunt: """
                      "\n1. Ziua de inceput: ", toate_listele[0][i],
                      "\n2. Luna de inceput: ", toate_listele[1][i],
                      "\n3. Anul de inceput: ", toate_listele[2][i],
                      "\n4. Ziua de sfarsit: ", toate_listele[3][i],
                      "\n5. Luna de sfarsit: ", toate_listele[4][i],
                      "\n6. Anul de sfarsit: ", toate_listele[5][i],
                      "\n7. Destinatia: ", toate_listele[6][i],
                      "\n8. Pretul: ", toate_listele[7][i])
    except ValueError:
        print("\nNu ati introdus un numar! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()                       

def cautare3():

    try:
        print("Zilele de sfarsit sunt: ", lista_data_sfarsit_zi)
        print("Lunile de sfarsit sunt: ", lista_data_sfarsit_luna)
        print("Anii de sfarsit sunt: ", lista_data_sfarsit_an)
        tiparire_zi_sfarsit = int(input("Alegeti ziua de sfarsit: "))
        tiparire_luna_sfarsit = int(input("Alegeti luna de sfarsit: "))
        tiparire_an_sfarsit = int(input("Alegeti anul de sfarsit: "))
        for i in range(0, len(lista_data_sfarsit_zi)):
            if tiparire_zi_sfarsit == lista_data_sfarsit_zi[i] and tiparire_luna_sfarsit == lista_data_sfarsit_luna[i] and tiparire_an_sfarsit == lista_data_sfarsit_an[i]:
                print("""\nPachetele cu cerintele selectate sunt: """
                      "\n1. Ziua de inceput: ", toate_listele[0][i],
                      "\n2. Luna de inceput: ", toate_listele[1][i],
                      "\n3. Anul de inceput: ", toate_listele[2][i],
                      "\n4. Ziua de sfarsit: ", toate_listele[3][i],
                      "\n5. Luna de sfarsit: ", toate_listele[4][i],
                      "\n6. Anul de sfarsit: ", toate_listele[5][i],
                      "\n7. Destinatia: ", toate_listele[6][i],
                      "\n8. Pretul: ", toate_listele[7][i])              
    except ValueError:
        print("\nNu ati introdus un numar! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()
                       

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

"""Functiile care fac rapoartele cerute"""

def raport1():

    try:
        print("Destinatiile valabile sunt: ", lista_destinatie)
        raport1_destinatie = input("Introduceti destinatia: ")
        for i in range(0, len(lista_destinatie)):
            if lista_destinatie[i] == raport1_destinatie:
                print("\nAvem in total", len(lista_destinatie[0:i+1]), "oferte pentru destinatia data!")                          
            else:
                print("Nu exista pachete cu cerinta data! Revenire la meniul principal...")
                meniu1()
                meniu_aplicatii()
    except ValueError:
        print("\nNu ati introdus un numar! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()

'def raport2():'

def raport3():
    
    try:
        print("Destinatiile valabile sunt(ron): ", lista_destinatie)
        raport3_destinatie = input("Introduceti destinatia: ")
        suma_pret = 0
        numar = 0
        for i in range(0, len(lista_destinatie)):
            if raport3_destinatie == lista_destinatie[i]:
                suma_pret = suma_pret + lista_pret[i]
                numar = numar + 1
        if numar != 0:
            media = suma_pret/numar
            print("Media preturilor pentru destinatia data este: ", media)
        else:
            print("Nu ati introdus o destinatie valida! Revenire la meniul principal...")
            meniu1()
            meniu_aplicatii()
    except ValueError:
        print("\nNu ati introdus un numar! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()            
            


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

"""Functiile care fac filtrarile cerute"""   
    
def filtru1():

    try:
        print("Destinatiile valabile sunt: ", lista_destinatie)
        print("Preturile valabile sunt: ", lista_pret)
        filtru1_pret = int(input("Introduceti pretul: "))
        filtru1_destinatie = input("Introduceti destinatia: ")
        for i in range(0, len(lista_pret)):
            if lista_pret[i] <= filtru1_pret and lista_destinatie[i] == filtru1_destinatie:
                print("""\nPachetele cu cerintele selectate sunt: """
                      "\n1. Ziua de inceput: ", toate_listele[0][i],
                      "\n2. Luna de inceput: ", toate_listele[1][i],
                      "\n3. Anul de inceput: ", toate_listele[2][i],
                      "\n4. Ziua de sfarsit: ", toate_listele[3][i],
                      "\n5. Luna de sfarsit: ", toate_listele[4][i],
                      "\n6. Anul de sfarsit: ", toate_listele[5][i],
                      "\n7. Destinatia: ", toate_listele[6][i],
                      "\n8. Pretul: ", toate_listele[7][i])   
            else:
                print("Nu exista pachete cu cerinta data! Revenire la meniul principal...")
                meniu1()
                meniu_aplicatii()
    except ValueError:
        print("\nNu ati introdus un numar! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()

def filtru2():

    
    try:
        print("Lunile valabile sunt: ", lista_data_inceput_luna)
        filtru2_luna = int(input("Introduceti luna nedorita: "))
        for i in range(0, len(lista_data_inceput_luna)):
            if filtru2_luna !=lista_data_inceput_luna[i]:                
                print("""\nPachetele cu cerintele selectate sunt: """
                      "\n1. Ziua de inceput: ", toate_listele[0][i],
                      "\n2. Luna de inceput: ", toate_listele[1][i],
                      "\n3. Anul de inceput: ", toate_listele[2][i],
                      "\n4. Ziua de sfarsit: ", toate_listele[3][i],
                      "\n5. Luna de sfarsit: ", toate_listele[4][i],
                      "\n6. Anul de sfarsit: ", toate_listele[5][i],
                      "\n7. Destinatia: ", toate_listele[6][i],
                      "\n8. Pretul: ", toate_listele[7][i])   
            else:
                print("Nu exista pachete cu cerinta data! Revenire la meniul principal...")
                meniu1()
                meniu_aplicatii()
    except ValueError:
        print("\nNu ati introdus un numar! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

"""Functia care realizeaza Undo"""

'def undo_function():'


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

"""Alegerea unuia dintre sub-meniuri(functia secundara-duce la toate functiile operante)"""

def sub_meniu_adaugare():
    try:
        adaugare = int(input("Ce sub-meniu din Alegere doriti sa accesati?(1 sau 2) "))
        if adaugare == 1:
            lista_adauga_zi_inceput()
            lista_adauga_luna_inceput()
            lista_adauga_an_inceput()
            lista_adauga_zi_sfarsit()
            lista_adauga_luna_sfarsit()
            lista_adauga_an_sfarsit()
            lista_adauga_destinatie()
            lista_adauga_pret()
            meniu1()
            meniu_aplicatii()
        
        elif adaugare == 2:
            modificare = int(input("""
                               1. Zi inceput
                               2. Luna inceput
                               3. An inceput
                               4. Zi sfarsit
                               5. Luna sfarsit
                               6. An sfarsit
                               7. Destinatie
                               8. Pret
Ce vrei sa schimbi? """))
      
            if modificare == 1:
                modificare_zi_inceput()
                print("\nNoua lista de zi inceput este: ", lista_data_inceput_zi)
            elif modificare == 2:
                modificare_luna_inceput()
                print("\nNoua lista de luna inceput este: ", lista_data_inceput_luna)
            elif modificare == 3:
                modificare_an_inceput()
                print("\nNoua lista de an inceput este: ", lista_data_inceput_an)
            elif modificare == 4:
                modificare_zi_sfarsit()
                print("\nNoua lista de zi sfarsit este: ", lista_data_sfarsit_zi)
            elif modificare == 5:
                modificare_luna_sfarsit()
                print("\nNoua lista de luna sfarsit este: ", lista_data_sfarsit_luna)
            elif modificare == 6:
                modificare_an_sfarsit()
                print("\nNoua lista de an sfarsit este: ", lista_data_sfarsit_an)
            elif modificare == 7:
                modificare_destinatie()
                print("\nNoua lista cu destinatii este: ", lista_destinatie)
            elif modificare == 8:
                modificare_pret()
                print("\nNoua lista cu preturi este: ", lista_pret)
            elif modificare > 8 or modificare < 1:
                print("Nu ati ales un meniu! Revenire la meniul principal...")
                meniu1()
                meniu_aplicatii()
        else:
            print("Nu ati ales un meniu! Revenire la meniul principal...")
            meniu1()
            meniu_aplicatii()            
    except ValueError:
        print("Nu ati ales un meniu! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()
    meniu1()
    meniu_aplicatii()
        
def sub_meniu_stergere():
    try:
        stergere = int(input("Ce sub-meniu din Stergere doriti sa accesati?(momentan doar 1 si 3) "))
        if stergere == 1:
            stergere1()
        elif stergere == 3:
            stergere3()
        else:
            print("Nu ati introdus o optiune valida! Revenire la meniul principal...")
            meniu1()
            meniu_aplicatii()
    except ValueError:
        print("Nu ati introdus o optiune valida! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()
    meniu1()
    meniu_aplicatii()
    
    
    
def sub_meniu_cautare():
    try:
        cauta = int(input("Ce sub-meniu din Cautare doriti sa accesati? "))
        if cauta == 1:
            cautare1()
        if cauta == 2:
            cautare2()
        elif cauta == 3:
            cautare3()
        else:
            print("Nu ati introdus o optiune valida! Revenire la meniul principal...")
            meniu1()
            meniu_aplicatii()
    except ValueError:
        print("Nu ati introdus o optiune valida! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()
    meniu1()
    meniu_aplicatii()
    
def sub_meniu_raport():
    
    try:
        raport = int(input("Ce sub-meniu din Raport doriti sa accesati?(momentan doar 1 si 3) "))
        if raport == 1:
            raport1()
        elif raport == 3:
            raport3()
        else:
            print("Nu ati introdus o optiune valida! Revenire la meniul principal...")
            meniu1()
            meniu_aplicatii()
    except ValueError:
        print("Nu ati introdus o optiune valida! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()
    meniu1()
    meniu_aplicatii()

    
    
def sub_meniu_filtrare():

    try:
        filtru = int(input("Ce sub-meniu din Filtrare doriti sa accesati? "))
        if filtru == 1:
            filtru1()
        if filtru == 2:
            filtru2()
        else:
            print("Nu ati introdus o optiune valida! Revenire la meniul principal...")
            meniu1()
            meniu_aplicatii()
    except ValueError:
        print("Nu ati introdus o optiune valida! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()
    meniu1()
    meniu_aplicatii()
        
    
def sub_meniu_undo():
    try:
        undo = int(input("Ce sub-meniu din Undo doriti sa accesati?(1) "))
        if undo == 1:
            verificare_undol = input("Sigur doriti sa realizati Undo?(da sau nu) ")
            if verificare_undol == 'da':
                print("Ati facut Undo! Revenire la meniul principal...")
                meniu1()
                meniu_aplicatii()
                """de adaugat aici functia pt undo"""
            elif verificare_undol == 'nu':
                print("Nu ati facut Undo! Revenire la meniul principal...")
                meniu1()
                meniu_aplicatii()
            else:
                print("Nu ati introdus o optiune valida! Revenire la meniul principal...")
                meniu1()
                meniu_aplicatii()
    except ValueError:
        print("Nu ati introdus o optiune valida! Revenire la meniul principal...")
        meniu1()
        meniu_aplicatii()
    meniu1()
    meniu_aplicatii()
        
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

"""Alegerea unuia dintre meniuri(functia principala)"""    

def meniu_aplicatii():
 
    alegere_meniu1 = True
    while alegere_meniu1:
        alegere_meniu1 = input("Ce meniu doriti sa accesati? ")
        if alegere_meniu1 == "adauga":
            meniu_adaugare()
            sub_meniu_adaugare()
            break
        elif alegere_meniu1 == "sterge":
            meniu_stergere()
            sub_meniu_stergere()
            break      
        elif alegere_meniu1 == "cauta":
            meniu_cautare()
            sub_meniu_cautare()
            break
        elif alegere_meniu1 == "raport":
            meniu_rapoarte()
            sub_meniu_raport()
            break
        elif alegere_meniu1 == "filtru":
            meniu_filtrare()
            sub_meniu_filtrare()
            break
        elif alegere_meniu1 == "undo":
            meniu_undo()
            sub_meniu_undo()
            break   
        elif alegere_meniu1 == "exit":
            print("Va multumim ca ati folosit serviciile noastre!")
            alegere_meniu1 = None
        else:
            print("Nu ati ales niciun meniu! Revenire la meniul prinipal...")

meniu_aplicatii()

