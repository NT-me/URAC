# URAC
Uvsq RISC Assembleur Compilateur, compilateur écrit en python permettant de tester les codes assembleur écrit dans le module d'HPC de L3

## Installation
### Pré-requis
  - Python 3

### Instruction
1. Si vous avez git d'installer : `git clone https://github.com/gnouf1/URAC.git` SINON  
Téléchargez l'archive et extrayez-la, durant les instructions ce dossier ce nommera "URAC-master"

2. Ensuite dans les deux cas aller dans le dossier URAC-master

3. Double cliquez sur "main.py" ou ouvrez-le grâce à la commande `python main.py`

## Utilisation
Une fois URAC installé vous pouvez écrire un fichier texte, un peu à la façon du fichier "test.txt" se trouvant dans le dossier URAC-master.
Pour l'exécuter :
1. Une fois URAC lancez (lorsqu'une console vous demandera le chemin du fichier)

2. Mettez le chemin jusq'à votre fichier (sans oublier son extension !)

3. Vous aurez alors un resultat en 3 parties, la première nommée "--- Python (approx) Conversion ---" affiche l'équivalent en python approximatif de votre code. Ensuite une seconde partie avec les valeurs des registres et tout en bas les valeurs sauvegardées dans la mémoire.

## Rappel
Si vous voulez vous renseigner sur les jeu d'instruction utilisé il est décrit dans "jeu.json"
