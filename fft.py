import numpy as np
global N

#must have length as factor of 2
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#should go to 2
N = len(x)

global final
final = 0

print("\n \n \n \n \n")

def sum(until, k, a, c, p):
    z = 2*p
    print("N/" + str(z) + " = " + str(until))
    if (until == 1):
        index = a
        print(index)
        return x[index] * np.exp((-1j * np.pi * k))
    else:
        #even
        print("creating even branch")
        even = sum(until/2, k, a, 2*c, p+1)

        #odd - difference is a vs a + p
        print("creating odd branch")
        odd = sum(until/2, k, a+p, 2*c, p+1)
        return even + odd

final = sum(N/2, 3, 0, 1, 1)
