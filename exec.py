#sys pour acceder au argument de la commande line
import sys

def inverser_chaine(chaine):
    return chaine[::-1]

if len(sys.argv) > 1:
    chaine_recuperee = ' '.join(sys.argv[1:])
    chaine_recuperee = chaine_recuperee.swapcase()
    #chaine_recuperee = chaine_recuperee[::-1]
    chaine_recuperee = inverser_chaine(chaine_recuperee)
    print(chaine_recuperee)
else:
    print("gay")
