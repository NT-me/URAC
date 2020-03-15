import json


def load_jeu(nom_jeu = "RISC_UVSQ"):
    J = open("jeu.json")
    jeu = json.load(J)
    res = list()

    # Future fonctionnalité
    jeu_courant = jeu[nom_jeu]

    for u in jeu_courant:
        o = u.split(" ")
        res.append(o)
    return res


def lexe(listParse):
    """
    Prend en paramètre la liste des lignes et renvoie une liste de liste avec les lexem
    """
    JEU = load_jeu()
    erreur = False
    res = list()

    for i in listParse:
        listI = i.split(" ")
        # Vérifie que l'opérande existe dans le jeu
        for operande in JEU:
            if not listI[0] in operande:
                erreur = True
            else:
                erreur = False
                break

        if erreur:
            print("Erreur de synthaxe ligne : \n => {}".format(i))
            quit()
        else :
            res.append(listI)

    return res
