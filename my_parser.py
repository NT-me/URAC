def parse(path):
    """
    Permet de parser le fichier de code 'path' et renvoie un tableau avec chaque ligne dans une case

    Param:
    path : str chemin d'accès au fichier

    Return:
    res : liste de str
    """
    res = list()
    file = open(path, 'r')

    ligne = True

    # Lit tout le fichier, ligne par ligne
    while ligne:
        ligne = file.readline()
        if ligne != "":
            res.append(ligne.replace("\n", ""))

    file.close()
    return res
