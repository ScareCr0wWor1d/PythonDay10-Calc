# Calc

from art import logo

def add(un, deux):
    return un + deux

def sub(un, deux):
    return un - deux

def multi(un, deux):
    return un * deux

def div(un, deux):
    return un / deux


operation = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div
}

def calculatrice():
    print(logo)
    frst_num = int(input("Entrer le premier chiffre de l'opération : "))
    if frst_num == 0:
        exit()
    end_of_calc = False

    while not end_of_calc:
        for ops in operation:
            print(ops)
        sign = input("Entrer quelle opération vous voulez effectuer : ")
        fonc_calc = operation[sign]
        scnd_num = int(input("Entrer le deuxième chiffre de l'opération : "))
        total = fonc_calc(frst_num, scnd_num)
        print(f"Votre calcul est {frst_num} {sign} {scnd_num} = {total}")
        if input(f"Voulez-vous continuer les opérations avec {total} (o/n) : ") == 'n':
            calculatrice()
        else:
            frst_num = total

calculatrice()