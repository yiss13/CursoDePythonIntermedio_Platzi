import os
import random


def words():
    words = []

    with open("./archivos/data.txt", "r", encoding="utf-8") as f:

        for word in f:
            words.append(word.upper().strip())
    
    return words


def run():
    data = words()
    word = random.choice(data)
    wordLettersList = [letter for letter in word]
    underscoresList = ["_"] * len(wordLettersList)
    letterIndexDict = {}
    
    for index, letter in enumerate(word):
        
        if not letterIndexDict.get(letter):
            letterIndexDict[letter] = []
            
        letterIndexDict[letter].append(index)

    while True:
        os.system("cls")
        print("¡Adivina la palabra!")
        
        for underscore in underscoresList:
            print(underscore + " ", end="")

        print("\n")
    
        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Sólo puedes ingresar letras."

        if letter in wordLettersList:

            for index in letterIndexDict[letter]:
                underscoresList[index] = letter
        
        if "_" not in underscoresList:
            os.system("cls")
            print("¡Ganaste!")
            print("La palabra era:", word)
            break


if __name__ == "__main__":
    run()