from main import nom_du_jeu as NDJ
exec("from jeux_fonctions import {} as JF".format(NDJ))


def codeGen(lexemList, nom_jeu="RISC_UVSQ"):
    c = list()
    for ligne in lexemList:
        operande = ligne[0]

        params = ""
        taille = len(ligne)
        i = 1
        while i < taille:
            if i == 1:
                params = params + "'" + ligne[i] + "'"
            else:
                params = params+',' + "'" + ligne[i] + "'"
            i = i + 1
        tmp = operande+'('+params+')'
        c.append(eval("JF.{}".format(tmp)) + "\n")

    return c
