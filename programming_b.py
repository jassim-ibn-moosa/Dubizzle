import random

# Function that returns a random integer number between 1 and 5 
def rand_int1():
    return random.randint(1,5)

# Function that creates a random integer between 1 and 7
def rand_int2(l, h):
    print 'Radnom number between 1 and 7--> %3d'% random.randint(l,h)

def main():
    fun_1 = rand_int1()
    print "Random number between 1 and 5--> %3d"% fun_1
    rand_int2(1,7)

if __name__ == '__main__':
    main()
