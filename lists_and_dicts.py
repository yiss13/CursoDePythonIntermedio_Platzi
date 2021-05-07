def run():
    myList = [1, "Hello", True, 4.5]
    myDict = {"firstname": "Yisselle", "lastname": "Vargas"}

    superList = [
        {"firstname": "Yisselle", "lastname": "Vargas"},
        {"firstname": "Tomas", "lastname": "Vargas"},
        {"firstname": "Alejandra", "lastname": "Uribe"},
        {"firstname": "Juliana", "lastname": "Vargas"},
        {"firstname": "Julieth", "lastname": "Vargas"}
    ]

    superDict = {
        "naturalNums": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "integerNums": [-2, -1, 0, 1, 2],
        "floatingNums": [1.2, 4.5, 6.3, 2.7, 3.8]
    }

    for key, value in superDict.items():
        print(key, "-", value)

    for dicts in superList:
        print(dicts)
        

if __name__ == "__main__":
    run()