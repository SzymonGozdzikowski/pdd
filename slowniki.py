

k = {
    "nazwa": "Władca pierścieni",
    "liczbaStron": 300
}


o = {
    "nazwa": "Hobbit",
    "liczbaStron": 350
}
    


# ---------------------------------------------------------
def inf(dc):
    for k,v in dc.items():
        print(f"{k}:  {v}")



# ----------------------------------------------------------
def edycja(dc):
    print("wprowadz klucz jaki chcesz edytować")
    print("==="*25)
    inf(dc)
    print("==="*25)
    inp = input()
    dc[inp] = input("Podaj nowe dane")





def edycja_listy(lst):
    while True:
        print(lst)
        print('a - dodaj element')
        print('u - usun element')
        print('e - wyjdz z edycji list')
        inp = input()
        if 'a' == inp:
            ocena = float(input())
            lst.append(ocena)
            print('ocena dodana')
        elif 'u' == inp:
            ocena = float(input())
            lst.remove(ocena)
            print('ocena usunieta')
        elif 'e' == inp:
            break
        else:
            print("Nie ma takiej komendy")


def dodaj_nowe_oceny(dc):
    print("Edytuj oceny")
    print("Matematyka - a")
    print("Angielski - b")
    print("Polski - c")
    inp = input()
    if inp == 'a':
        edycja_listy(dc['matematyka'])
    elif inp == 'b':
        edycja_listy(dc['angielski'])
    elif inp == 'c':
        edycja_listy(dc['polski'])
    print("dodaj_nowe_oceny - zakonczylo dzialnie")
   

# ----------------------------------------------------------
while True:
    print("==="*25)
    print("e - wyjdź z programu")
    print("i - informacje o ksiazkach")
    print("ed - edytuj dane")
    print("oc - edytuj oceny")
    print("==="*25)
    inp = input().lower()
    if 'e' == inp:
        break
    elif 'i' == inp:
        inf(k)
    elif 'ed' == inp:
        edycja(k)
    elif 'oc' == inp:
        dodaj_nowe_oceny(k)
    else:
        print("Program zkonczyl dziłanie")
        break
