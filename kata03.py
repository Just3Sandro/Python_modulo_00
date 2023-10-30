kata = "The right format"

c = "-"
i = len(kata)
print(i)
if i == 42:
    print(kata)
elif i < 42:
    j = 42 - i
    print(j)
    ligne = c * j
    print(ligne + kata)
