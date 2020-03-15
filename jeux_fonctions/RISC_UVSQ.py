def LI(R, O):
    res = "{} = {}".format(R, O)
    return res


def ADD(R0, R1, R2):
    res = "{} = {} + {}".format(R2, R0, R1)
    return res


def SUB(R0, R1, R2):
    res = "{} = {} - {}".format(R2, R0, R1)
    return res


def DIV(R0, R1, R2):
    res = "{} = {} / {}".format(R2, R0, R1)
    return res


def MULT(R0, R1, R2):
    res = "{} = {} * {}".format(R2, R0, R1)
    return res


def OR(R0, R1, R2):
    res = "{} = {} or {}".format(R2, R0, R1)
    return res


def AND(R0, R1, R2):
    res = "{} = {} and {}".format(R2, R0, R1)
    return res


def SLT(R0, R1, R2):
    res = "if {} < {}:\n    {} = 1\nelse:\n    {} = 0".format(R0, R1, R2, R2)
    return res


def LW(R1, R2, O):
    res = "{} = MEM[{} + {}]".format(R2, R1, O)
    return res


def SW(R1, R2, O):
    sto = "\'{}:\'+str({})".format(R2, R2)
    res = "MEM[{} + {}] = {}".format(R1, O, sto)
    return res


def JUMP(R0, O):
    nb_l = int(O)/2
    nb_l = int(nb_l)
    O.replace("+", "")
    res = "CO = CO + ({} + {})".format(R0, nb_l)

    return res


def BNEZ(R0, R1, O):
    nb_l = int(O)/2
    if type(nb_l) != type(2):
        # Cas où ce n'est pas un multiple de deux
        print("ERREUR FATAL : Offset d'un bnez n'est pas un nombre pair !")
        quit()
