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
    erreur0 = False
    for i in listParse:
        listI = i.split(" ")
        # Vérifie que l'opérande existe dans le jeu
        for operande in JEU:
            if not listI[0] in operande:
                # Cas où l'opérande n'est pas trouvée
                erreur = True
            else:
                ite = 0
                # Cas où l'opérande est trouvée
                if len(operande) != len(listI):
                    erreur = True
                    break
                else:
                    # Cas où il y'a le bon nombre de paramètre
                    for p in operande:
                        if p[:1] == 'R' and listI[ite][:1] != 'R':
                            # Cas où il devrait y avoir un registre mais il n'y en a pas
                            erreur0 = True
                            break
                        if p[:1] == 'O' and listI[ite][:1] == 'R':
                            # Cas où il devrait y avoir un offset mais il y a un registre
                            erreur0 = True
                            break
                        ite = ite + 1

                erreur = False
                if erreur0:
                    break
                break

        if erreur or erreur0:
            print("Erreur de synthaxe ligne : \n => {}".format(i))
            quit()
        else:
            res.append(listI)

    return res
