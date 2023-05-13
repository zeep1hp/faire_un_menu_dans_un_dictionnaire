def game1():
    c = 1+1
    return True,c
def game2():
    c = 2+2
    return True,c
def game3():
    c = 3+3
    return True,c
def game4():
    c = 4+4
    return True,c

menu = {
    '1': game1(),
    '2': game2(),
    '3': game3(),
    '4': game4()
}


x = input("[1] JEU1\n[2] JEU2\n[3] JEU3\n[4] JEU4\n==>")
for cle, valeur in menu.items():
    if x == cle:
        v, resultat = valeur
        if v is True:
            print("JEU "+cle )
            print(f"resultat : {resultat}")
           
    
          

    