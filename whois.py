import sys

if len(sys.argv) == 2:
    chaine_recup = int(sys.argv[1])
    if (chaine_recup == 0):
        print("je suis 0")
    elif (chaine_recup % 2 == 0):
        print("Im even")
    else:
        print("Im Odd")
else:
    print("gay")
