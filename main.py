import my_parser as P
import my_lexer as L

if __name__ == "__main__":
    path = input("Entrez le chemin du fichier à compiler :")

    listParse = list()

    try:
        listParse = P.parse(path)
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
    print(listParse)

    lexemList = L.lexe(listParse)
    print(lexemList)
