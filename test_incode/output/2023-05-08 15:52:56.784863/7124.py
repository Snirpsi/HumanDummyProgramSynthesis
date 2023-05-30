#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that removes fruits.
    while True:
        fruirs.remove("apple")
        fruirs.remove("banana")
        fruirs.remove("orange")
        if fruirs == []:
            break
        else:
            print("Fruits: ", fruirs)

