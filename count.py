import sys
#if len(sys.argv) == 2:
#    text = sys.argv[1]

def text_analyzer(text=None):
    #if len(sys.argv) == 2:
     #   text = sys.argv[1]
    if text is None:
        text = input("Entrez un text :")
    nb_chara = len(text)
    nb_maj = sum(1 for char in text if char.isupper())
    nb_min = sum(1 for char in text if char.islower())
    nb_dots = text.count('.')
    nb_space = text.count(' ')
    print(f"le nombre de char est : {nb_chara} le nombre de maj: {nb_maj}, nb min: {nb_min} nb space : {nb_space}")
if __name__ == "__main__":
    text_analyzer()

#if __name__ = "__name__":
#check if command-line arguments are provided
#if len(sys.argv)==2:
#   input_text = sys.argv[1]
#else:
#   if no arguments prompt the user for input
#   input_text = input("enter a text: ")
