def print_privet(name):
    """"Print privetstvie"""
    print("congratulation " + name + " wish you all the best!")


def summa(x, y):
    return x+y


def factorial(x):
    """Calculate Factorial number x"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
        return otvet


# ------------------
print("--------------------------")
print_privet("Vova")
print_privet("peta")
print_privet("Ivan")
x = summa(33, 22)
print(x)

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

