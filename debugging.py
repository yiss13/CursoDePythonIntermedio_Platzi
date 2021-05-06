def divisors(num):
    divisors =[]
    try: 

        if num < 0:
            raise ValueError("No se pueden ingresar números negativos")
        
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)

        return divisors

    except ValueError as ve:
        print(ve)

        return False


def run():

    try:
        num = int(input("Ingresa un número: "))

        # if num < 0:

        #     raise ValueError

        print(divisors(num))
        print("¡Terminó el programa!")

    except ValueError:
        print("Debe ingresar un número")



if __name__ == "__main__":
    run()