import sys
#if not isinstance(sys.argv[1], int):
 #   print("Only integer is accepted")
#else:
if (len(sys.argv) == 3):
    #a = int(sys.argv[1])
    #b = int(sys.argv[2])
#    if not a.isdigit():
#        print("the argument is not an inteeger")
   #     sys.exit(1)
   # if not b.isdigit():
    #    print("the argument is not an inteeger")
     #   sys.exit(1)        
    if sys.argv[1].isdigit() or sys.argv[2].isdigit():
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = a + b
        print(f"Sum : {c}")
        c = a - b
        print(f"Sum : {c}")
        c = a * b
        print(f"Sum : {c}")
        if (not a or not b):
            print("Quotient: ERROR (division by zero)")
            print("Remainder: ERROR (modulo by zero)")
        else:
            c = a / b
            print(f"Sum : {c}")
            c = a % b
            print(f"Sum : {c}")
    else:
        print("ERROR : only integer")
elif(len (sys.argv) < 3):
    print(f"Usage: <number 1> <number 2>")
elif(len (sys.argv) > 3):
    print(f"Too many argument")
