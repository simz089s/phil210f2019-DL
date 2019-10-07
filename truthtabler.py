

try:
    n = int(input("How many atomic sentences? "))
    S = input("Input sentence: ")

    print()
    [print(" P{} |".format(i+1), end='') for i in range(n)]
    print(' ', S)
    [print("-", end='') for i in range(n*5-1)]
    print('|', end='')
    [print("-", end='') for i in range(len(S)+4)]
    print()

    for i in range(2**n):
        current_vals = []
        for j in range(n):
            current_vals.append( (i // (2**j)) % 2 )
            print(' ', current_vals[j], '|', end='')
        ### CUSTOM ###
        P = current_vals[0]
        Q = current_vals[1]
        full = not P or Q == (not not Q) or not P
        print("     {}  {}  {} {} {}".format(not P or Q, full, not Q, not not Q or not P, not P).replace("True", 'T').replace("False", 'F'))
        ##############
finally:
    input()
