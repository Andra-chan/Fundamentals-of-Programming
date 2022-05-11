def creeaza_baller(ident, nume, valoare):
# functie care creeaza un baller pe baza identificatorului ident intreg, a numelui nume string si a valorii reale val
# date de intrare: ident - in numar intreg
#                 nume - string
#                 valoare - float
# date de iesire: baller - un baller cu identificatorul ident, numele nume si valoarea valoare
        return{
            "ident":ident,
            "nume":nume,
            "valoare":valoare
            }

def get_ident(baller):
# functie care returneaza identificatorul intreg al baller-ului baller
# date de intrare: baller - baller
# date de iesire: ident - intregul care reprezinta identificatorul baller-ului
    return baller["ident"]

def get_nume(baller):
# functie care returneaza numele baller-ului baller
# date de intrare: baller - baller
# date de iesire: nume - stringul care reprezinta numele baller-ului
    return baller["nume"]

def get_valoare(baller):
    return baller["valoare"]


def set_valoare(baller, valoare_noua):
    baller["valoare"] = valoare_noua

def egal_ballers(baller0, baller1):
    return get_ident(baller0) == get_ident(baller)
    
def valideaza_baller(baller):
# functie care verifica daca identificatorul intreg al ballerului e pozitiv
# daca numele ballerului e nevid si daca valoarea reala a ballerului este cuprinsa intre 0 si 10000
# date de intrare: baller - baller-ul care trebuie validat
# date de iesire: -
# ridica Exceptie (*) de tipul Exception cu textul:
#           "ident invalid!\n" - daca identificatorul ballerului nu este pozitiv
#           "nume invalid!\n" - daca numele e vid
#           "valoare invalida!\n" - daca valoarea < 0 sau > 10000
    erori = ""
    if get_ident(baller) <= 0:
        eror += "ident invalid!\n"
    if get_nume(baller) == "":
        erori += "nume invalid!\n"
    if get_valoare(baller) < 0 or get_valoare(baller) > 10000:
        erori += "valoare invalida!\n"
    if len(erori) > 0:
            raise Exception(erori)
           
            

def test_valideaza_baller():
    baller = creeaza_baller(-23, "gigi", 56)
    try:
        valideaza_baller(baller)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "ident invalid!\n")
    baller1 = creeaza_baller(-23, "", 23456)
    try:
        valideaza_baller(baller1)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "ident invalid!\nnume invalid!\nvaloare invalida!\n")
    baller = creeaza_baller(23, "jordan", 9000.1)
    valideaza_baller(baller)


def test_creeaza_baller():
    baller = creeaza_baller(23, "jordan", 9000.1)
    assert(get_ident(baller) == 23)
    assert(get_nume(baller) == "jordan")
    assert(abs(get_valoare(baller)-9000.1)<0.000001)
    set_valoare(baller, 9000.23)
    assert(abs(get_valoare(baller)-9000.23)<0.000001)

def adauga_lista_unic(lista,elem):
# functie care adauga un element intr-o lista de elemente de acelasi tip cu el, unic identificabile prin ident
# in lista nu este permis sa existe doua elemente cu acelasi ident
# date de intrare: lista - o lista de elemente de tipul elementului elem
#                  elem - elementul care trebuie introdus in lista lista daca nu mai exista deja un element cu acelasi ident in lista
# date de iesire: - daca nu exista vreun element in lista cu identul lui elem
#                   lista' = lista U {elem}
# ridica exceptie (**) de tipul Exception cu textul:
#                                       - "identexistent!\n" - daca exista deja un element cu ident respectiv in lista
    for el in lista:
        if egal_ballers(el, elem):
            raise Exception("ident existent!\n")
    lista.append(elem)

def test_adauga_lista_unic():
    l = []
    baller = creeaza_baller(23, "jordan", 9000.1)
    adauga_lista_unic(l, baller)
    assert (len(l) == 1)
    assert(egal_ballers(baller, l[0]))
    baller1 = creeaza_baller(23, "lebum", 789.67)
    try:
        adauga_lista_unic(l, baller1)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "ident existent!\n")

def srv_adauga_baller_lista(lista_balleri, ident, nume, valoare):
# functie care pe baza unui identificator intreg ident, a unui nume string nume si a unei valori reale valoare
# construieste un baller cu aceste date, verifica daca ident >0, numele e nevid si valoarea reala e cuprinsa
# intre 0 si 10000 si daca ident nu mai este prezent la niciun baller din lista_balleri adauga ballerul nou-creat
# in lista_balleri
# date de intrare: lista baller - o lista de balleri cu ident unci
#                  ident - un numar intreg
#                  nume - string
#                  valoare - float
# date de iesire: -
#               daca ballerul e adaugat cu succes:
# ridica exceptie de tipul Exception cu textul:
#                           - exceptie de validare (*) daca ballerul nu este valid
#                           - exceptie de adaugare la lista (**) daca identul apare deja in lista_balleri
    baller = creeaza_baller(ident, nume, valoare)
    valideaza_baller(baller)
    adauga_lista_unic(lista_balleri, baller)
    
    

def test_srv_adauga_baller_lista():
     lista = []
     srv_adauga_baller_lista(lista, 23, "jordan", 9000.1)
     assert(len(lista) == 1)
     assert(egal_ballers(lista[0], creeaza_baller(23, "jordan", 9000.1)))
     try:
        srv_adauga_baller_lista(lista, -23, "gigi", 20000)
        assert(False)
     except Exception as ex:
        assert(str(ex) == "ident invalid!\nvaloare invalida!\n")
     try:
        srv_adauga_baller_lista(lista, 23, "lebum", 789)
        assert(False)
     except Exception as ex:
        assert(str(ex) == "ident existent!\n")

def ui_adauga_baller(lista_balleri):
    ident = int(input("Introduceti ident: "))
    nume = input("Introduceti nume: ")
    valoare = float(input("Introduceti valoarea: "))
    srv_adauga_baller_lista(lista_balleri, ident, nume, valoare)

def run():
    lista_balleri = []
    comenzi = {}
    while True:
        cmd = input(">>>")
        if cmd == "exit":
            print("Sayonara, sucksa!")
            return
        if cmd in comenzi:
            try:
                comenzi[cmd](lista_balleri)
            except ValueError as ve:
                print("Format numeric invalid!")
            except Exception as ex:
                print(ex)
        else:
            print("Comanda invalida!")
     

def run_all_tests():
    test_creeaza_baller()
    test_valideaza_baller()
    test_adauga_lista_unic()
    test_srv_adauga_baller_lista()

run_all_tests()
