def print_larger(a, b):

    ''' prints the larger of the two numbers
    The two values must be Integers '''

    # convert to integers, if possible

    a = int(a)
    b = int(b)

    if a > b:
        print("a : %d is larger than b : %d " % (a, b))
    elif a < b:
        print("b : %d is larger than a : %d " % (b, a))
    else:
        print("a : %d and b : %d are equal " % (a, b))


def print_largest(a, b, *args):
    '''prints the largest of the input values
    The input values must be Integers '''

    #convert to integers if possible

    a = int(a)
    b = int(b)
    if(a > b):
        largest = a
        print("a : %d is the larger of a & b" % a)
    else:
        largest = b
        print("b : %d is the larger of a & b " % b)

    print("args = ", args)
    for i in args:
        if largest < int(i):
            largest = int(i)
    return largest

