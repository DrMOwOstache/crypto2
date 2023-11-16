def getInteger():
    """
    gets the integer for the algorithm
    """
    n = 0
    ok = 0
    while ok == 0:  # checks if you input a correct integer
        try:
            n = int(input("Write an integer: "))
            ok = 1
        except ValueError:
            print("!Please input an integer!")
    return n


def getFunction(n):
    """
    gets the function you want to use in Pallard's Algorithm
    if mothing is put then the default function is used: f(x) = x^2+1
    """
    print("Rules: \n"
          "\t> you can write only the constants\n")
    inputContants = [0]
    ok = 0
    while ok == 0:  # checks if you input a correct list of integer
        try:
            inputContants = input("Please enter the list of constants separated by spaces: ")
            listOfConstants = inputContants.split()
            for i in range(len(listOfConstants)):
                listOfConstants[i] = int(listOfConstants[i])
            ok = 1
        except ValueError:
            print("!Please input an integer!")

    func = lambda x, n: Polynomial(x, listOfConstants) % n
    PollardAlgorithm(n, func)


def Polynomial(x, listOfConstants):
    """
    :param x: root
    :param listOfConstants: the list of constants that are in the reverse order of the powers
    :return: the result of the polynomial
    """
    power = len(listOfConstants) - 1
    result = 0
    for i in range(len(listOfConstants)):
        result += (listOfConstants[i] * (x ** power))
        power -= 1
    return result


def PollardAlgorithm(n, func=lambda x, n: (x ** 2 + 1) % n):
    x = 2  ## starting value
    y = x
    d = 1

    # print(n)
    while d == 1:
        x = func(x, n)
        y = func(func(y, n), n)
        if x < y:
            d = gcd(y - x, n)
        else:
            d = gcd(x - y, n)
        # print("d = ", d)
        # print("x = ", x)
        # print("y = ", y)

    if d == n or d == 0:
        print("Failure")
    else:
        print("The non-trivial factor of ", n, " is: ", d)


def gcd(a, b):
    # print("a = ", a)
    # print("b = ", b)
    if a == 0 and b == 0:
        return -1

    if a == 0:
        return 0

    if b > a:
        return gcd(b, a)
    while b > 0:
        r = a % b
        a = b
        b = r
    return a
