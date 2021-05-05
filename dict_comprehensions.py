from math import sqrt

def run():
    # myDict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         myDict[i] = i ** 3
    
    # myDict = {i: i ** 3  for i in range(1, 101) if i % 3 != 0}
    myDict = {i: round(sqrt(i), 2) for i in range(1, 1001)}

    print(myDict)


if __name__ == "__main__":
    run()