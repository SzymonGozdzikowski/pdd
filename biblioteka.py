k = {
    "nazwa": "Władca pierścieni",
    "liczbaStron": 300
}
# ----------------------------------------
def inf(lst:list)->None:
    for dic in lst:
        for v,k in dic.items():
            print(f"{v} : {k}")
        print("---"*10)
# ----------------------------------------
biblioteka = [k,k,k,k,k,k,k,k]
while True:
    inp = input().lower()
    if inp == "i":
        inf(biblioteka)
    elif inp == "e":
        print("Program zakończy działanie")
        break
    else:
        print("Nie ma takiej komendy")


