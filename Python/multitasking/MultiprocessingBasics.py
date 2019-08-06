# -------------------------------------
# Learning to code with multiprocessing
# -------------------------------------

# Importing some standard modules...
from multiprocessing import Pool
    # ... for multiprocessing.
import time 
    # ... for interacting with system clock.

# A function raising an input to the 4th power
def f(x):
    return x*x*x*x

if __name__ == '__main__':
    # Some numbers to play with
    sampleList = [12, 345, 678, 901, 2345]
    
    # SERIAL PROCESSING
    serialStartTime = time.time()

    for number in sampleList:
        result = f(number)
        print(result)
    
    serialEndTime = time.time()
    print()

    # MULTIPROCESSING
    multiStartTime = time.time()
    
    p = Pool()
    result = p.map(f, sampleList)
    p.close()
    p.join()
    print(result)

    multiEndTime = time.time()
    print()

    print ("Single-core processing took: " + str((serialEndTime - serialStartTime) * 1000) + " milliseconds.")
    print ("Multi-core processing took: " + str((multiEndTime - multiStartTime) * 1000) + " milliseconds.")

# REFERENCE: https://www.youtube.com/watch?v=_1ZwkCY9wxk&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN&index=7
