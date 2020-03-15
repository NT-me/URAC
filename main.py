import my_parser as P
import my_lexer as L
import code_generator as CG

nom_du_jeu = "RISC_UVSQ"
NB_CASE = 1000


def exec_res(code):
    ca = 0
    ca0 = 0
    CO = 0

    MEM = list()
    taille_prog = len(code)

    while ca < NB_CASE:
        MEM.append(None)
        ca = ca + 1

    while CO < taille_prog:
        exec(code[CO])
        exec("print(CO)")
        print(code[CO])

        CO = CO + 1

    lst = dir()

    for i in lst:
        if i[:1] == 'R':
            print("{} = {}".format(i, eval(i)))

    print("--- WORD(s) IN MEMORY ---")

    for n in MEM:
        if n is not None:
            print("MEM[{}] = {}".format(ca0, n))
        ca0 = ca0 + 1


if __name__ == "__main__":
    path = input("Entrez le chemin du fichier à compiler :")

    listParse = list()

    try:
        listParse = P.parse(path)
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
    #print(listParse)

    lexemList = L.lexe(listParse)
    #print(lexemList)

    code = CG.codeGen(lexemList)
    exec_res(code)
