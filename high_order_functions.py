from functools import reduce

def run():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    odd = list(filter(lambda x: x % 2 != 0, myList)) #imprime los números impares
    squares = list(map(lambda x: x ** 2, myList)) #imprime los cuadrados de los números
    allMultiplied = reduce(lambda a, b: a * b, myList) #imprime la multiplicación de todos los números dentro de la lista
       
        # Forma de hacer la anterior línea con un for
        # my_list = [2, 2, 2, 2, 2] 
        # all_multiplied = 1
        # for i in my_list:
        #     all_multiplied = all_multiplied * i
        # print(all_multiplied)
        
    print(odd)
    print(squares)
    print(allMultiplied)

if __name__ == "__main__":
    run()