"""
This scratch file merely implements the Karatsuba multiplication algorithm. It is a recursive algorithm that
calculates the product of two n-digit integers.

Note that the following only works if n is even and the sum of 2 digits does not exceed 9
"""

n1 = 3141592653589793238462643383279502884197169399375105820974944592
n2 = 2718281828459045235360287471352662497757247093699959574966967627

n1_l = len(str(n1))
n2_l = len(str(n2))
print("Length of number1 = {}".format(n1_l))
print("Number1 = {}".format(n1))

print("Length of number2 = {}".format(n2_l))
print("Number2 = {}".format(n2))

def break_up(n1, n2, print_result = False):

    n1_string = str(n1)
    n2_string = str(n2)

    n1_splitter = int(len(n1_string)/2)
    # print(n1_splitter)
    n2_splitter = int(len(n2_string)/2)
    # print(n2_splitter)

    a = int(n2_string[:n2_splitter])
    b = int(n2_string[n2_splitter:])

    c = int(n1_string[:n1_splitter])
    d = int(n1_string[n1_splitter:])

    if print_result:
        print("a = {}".format(a))
        print("b = {}".format(b))
        print("c = {}".format(c))
        print("d = {}".format(d))

    return a, b, c, d


def intermediates(a, b, c, d, print_result):

    ac = multiply(a, c)
    bd = multiply(b, d)
    ad_bc = multiply(a, d) + multiply(b, c)
    return ac, bd, ad_bc


def multiply(n1, n2, print_result=False):
    n = len(str(n1))
    n_2 = len(str(n2))
    if n == 1 or n_2 == 1:
        return n1*n2
    else:
        a, b, c, d = break_up(n1, n2, print_result=print_result)

        ac, bd, ad_bc = intermediates(a, b, c ,d, print_result)

        product = (10**n)*ac + (10**(n/2))*ad_bc + bd
        if print_result:
            print("{} x {} = {}".format(n1, n2, product))

        return product


result = multiply(n1, n2, print_result=True)
print("To verify, {} x {} = {}".format(n1, n2, n1*n2))





