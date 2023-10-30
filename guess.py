import random

choice = input("This os an interactive guessing game!\n you have to enter a number between 1 and 99 to find out the secret number.\n type 'exit' to end the game.\n Good Luck!\n")

rdm_num = random.randint(1, 99)

while True:
    choice = input("What's your guess between 1 and 99?")
    if choice.lower() == 'exit':
        print("GOODBYE!")
        break
    try:
        nbr = int(choice)
        if nbr < 1 or nbr > 99:
            print("un nombre entre 1 et 99 svp!")
        if nbr == rdm_num:
            print("correct the secret number is", rdm_num)
            break
        elif nbr > rdm_num:
            print("Too high")
        elif nbr < rdm_num:
            print("Too low")
    except ValueError:
            print("fait un effort mon reuf")

