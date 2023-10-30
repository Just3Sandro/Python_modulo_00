kata = (0, 4, 132.42222, 10000, 12345.67)
#mettre un if avec si < 10 mettre un 0
module = "module_" + "_".join(map(str, [kata[0]]))
exo = "exo" + "_".join(map(str, [kata[1]]))
decimal1 = format(kata[2], ".2f")
decimal2 = format(kata[4], ".2e")
entier = format(kata[3], ".2e")
print(module + ", " + exo + " : " + decimal1 + entier + decimal2)
print(entier)
print(decimal1)
print(decimal2)

