def creeaza_baller(ident,nume,valoare) :
#creeaza un baller pe baza identificatorului ident int, numelui nume string si a valorii reale
#date de intrare: ident - nr intreg
#                             nume - string
#                             valoare - float
#date de iesire:   baller - un baller cu ident,nume,valoare
    return { "ident": ident, "nume": nume, "valoare": valoare }

def get_ident(baller) :
#functie care returneaza ident din baller
#date de intrare: baller - baller
#date de iesire: ident - nr intreg
    return baller["ident"]

def get_nume(baller) :
#functie care returneaza nume din baller
#date de intrare: baller - baller
#date de iesire: nume - string
    return baller["nume"]

def get_valoare(baller) :
#functie care returneaza valoare din baller
#date de intrare: baller - baller
#date de iesire: valoare - nr intreg
    return baller["valoare"]

def set_valoare(baller, valoare_noua) :
    baller["valoare"]=valoare_noua

def egal_ballers(baller0, baller1) :
    return get_ident(baller0)==get_ident(baller1)

def valideaza_baller(baller) :
#functie care verifica daca ident este pozitiv, daca numele este nevid 
#si daca valoarea reala este cuprinsa intre 0 si 10000
#date de intrare: baller - baller
#date de iesire: True - baller este valid
#ridica Exceptie cu textul:
#                                   "ident invalid!\n" - daca ident nu este pozitiv
#                                   "nume invalid!\n" - daca numele este vid
#                                   "valoare invalida!\n" - daca valoarea reala nu este cuprinsa in (0, 10000)
#                   (*)
    erori=""
    if get_ident(baller)<=0:
        erori +="ident invalid!\n"
    if get_nume(baller)=="":
        erori +="nume invalid!\n"
    if float(get_valoare(baller))<0 or float(get_valoare(baller))>10000 :
        erori += "valoare invalida!\n"
    if len(erori) > 0 :
        raise Exception(erori)

def to_string(baller):
    return str(get_ident(baller))+":"+get_nume(baller)+"["+get_valoare(baller)+"]"

def to_string_lista(lista):
    s = ""
    for elem in lista:
        s += to_string(elem)
    return s

def test_valideaza_baller() :
    baller = creeaza_baller( -23,'gigi',56 )
    try:
        valideaza_baller(baller)
        assert(False)
    except Exception as ex:
        assert( str(ex)=="ident invalid!\n")
    baller1 = creeaza_baller(-23,"", 23412)
    try:
        valideaza_baller(baller1)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="ident invalid!\nnume invalid!\nvaloare invalida!\n")
    baller = creeaza_baller( 23,'jordan', 9000.1 )
    valideaza_baller(baller)

def test_creeaza_baller() :
    baller = creeaza_baller( 23,'jordan', 9000.1 )
    assert( get_ident(baller)==23 )
    assert( get_nume(baller)=='jordan')
    assert( abs(get_valoare(baller) - 9000.1) < 0.00001 )
    set_valoare( baller,9000.23 )
    assert( abs(get_valoare(baller) - 9000.23) < 0.00001 )

def adauga_lista_unic(lista,elem) :
#functie care adauga un elem intr-o lista de elem de acelasi tip, unic identificabile prin ident
#in lista nu este permis sa existe doua elemente cu acelasi ident
#date de intrare: lista - o lista de elemente de tipul elementului
#                             elem - elementul care trebuie introdus in lista daca nu exista deja un element
#                                           cu acelasi ident in lista
#date de iesire: - daca nu exista vreun element in lista cu identificatorul lui elem,
#                               atunci lista' = lista U {elem}
#ridica exceptie de tipul Exception cu textul
#                               -"ident existent!\n" daca exista deja un elem in lista cu acelasi ident
#               (**)
    for el in lista:
        if egal_ballers(el, elem):
            raise Exception("ident existent!\n")
    lista.append(elem)

def test_adauga_lista_unic():
    l=[]
    baller = creeaza_baller(23,'jordan',9000.1)
    adauga_lista_unic(l,baller)
    assert(len(l)==1)
    assert(egal_ballers(baller, l[0]))
    baller1 = creeaza_baller(23, 'lebum', 789.42)
    try:
        adauga_lista_unic(l,baller1)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="ident existent!\n")

def srv_adauga_baller_lista( lista_balleri, ident, nume, valoare) :
#functie care pe baza unui ident int, nume string, valoare float construieste un baller
#cu aceste date, verifica ident>0, nume nevid si valoare intre 0 si 10000 si daca ident
#nu mai este la niciun baller din lista_balleri, adauga ballerul in lista_balleri
#date de intrare: lista_balleri - o lista de balleri cu ident unic
#                             ident - un nr intreg
#                             nume - string
#                             valoare - float
#date de iesire: -
#                           daca ballerul e adaugat cu succes
#ridica exceptie de tipul Exception:
#                           -exceptie de validare (*) daca ballerul nu e valid
#                           -exceptie de adaugare la lista (**) daca ballerul nu e valid
    baller = creeaza_baller(ident,nume,valoare)
    valideaza_baller(baller)
    adauga_lista_unic(lista_balleri,baller)
    

def test_srv_adauga_baller_lista():
    lista=[]
    srv_adauga_baller_lista(lista,23,'jordan',9000.1)
    assert(len(lista)==1)
    assert(egal_ballers(lista[0], creeaza_baller(23,'jordan',9000.1)))
    try:
        srv_adauga_baller_lista(lista,-23,'gigi',20000)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="ident invalid!\nvaloare invalida!\n")
    try:
        srv_adauga_baller_lista(lista,23,'lebum',789)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="ident existent!\n")

def ui_adauga_baller(lista_balleri):
    ident = int(input("ident:"))
    nume = input("nume:")
    valoare = input("valoare:")
    srv_adauga_baller_lista( lista_balleri, ident, nume, valoare)

def ui_print_ballers(lista_balleri):
    if len(lista_balleri)==0:
        print("nu exista balleri in lista")
        return
    print(to_string_lista(lista_balleri))

def run():
    lista_balleri=[]
    comenzi={"adauga_baller": ui_adauga_baller , "print_ballers":ui_print_ballers}
    while True:
        cmd = input(">>>")
        if cmd == "exit":
            print("Salutare!")
            return
        if cmd in comenzi:
            try:
                comenzi[cmd](lista_balleri)
            except ValueError as ve:
                print("input gresit!")
            except Exception as ex:
                print(str(ex))
        else:
            print("Comanda invalida!")

def run_all_tests() :
    test_creeaza_baller()
    test_valideaza_baller()
    test_adauga_lista_unic()
    test_srv_adauga_baller_lista()

run_all_tests()
run()
