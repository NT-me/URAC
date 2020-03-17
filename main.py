import my_parser as P
import my_lexer as L
import code_generator as CG
import time

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

    print("--- Python (approx) Conversion ---")
    while CO < taille_prog:
    #     print("CO " + str(CO))
    #
    #     lst = dir()
    #     for i in lst:
    #         if i[:1] == 'R':
    #             print("> {} = {}".format(i, eval(i)))
        print(code[CO])
        if 'JUMP' not in code[CO] and 'BNEZ' not in code[CO]:
            exec(code[CO])
            CO = CO + 1
        else:
            if 'JUMP' in code[CO]:
                J = code[CO].split(" ")
                CO = CO + (int(eval(J[1])) + int(J[2]))
            elif 'BNEZ' in code[CO]:
                B = code[CO].split(" ")
                if eval(B[2]) != 0:
                    CO = int(CO) + (int(eval(B[1])) + int(B[3])/2)
                    CO = int(CO)
                    # print("> R4 = {}".format(R4))
                    # print("> CO : {}".format(CO))
                    # print("> B[2] " + str(eval(B[2])))
                else:
                    CO = CO + 1

        #time.sleep(1)

    print("--- --- ---\n\n")
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
