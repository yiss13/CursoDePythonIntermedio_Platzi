def run():
    # squares = []
    # num = 0

    # for i in range(1, 101):

    #     if i % 3 != 0:
    #         squares.append(i ** 2)

    # squares = [i ** 2 for i in range(1, 101) if i % 3 != 0]
    multiples = [i for i in range(1, 100) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    
    odd = [i for i in multiples if i % 2 != 0]
    squares = [i ** 2 for i in multiples]


    print(multiples)
    print(odd) # imprime números impares
    print(squares) # imprime el cuadrado de los número


if __name__ == "__main__":
    run()