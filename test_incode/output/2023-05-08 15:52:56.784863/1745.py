#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that removes fruits.
    def removeFruits(fruits):
        fruits.remove("apple")
        fruits.remove("banana")
        fruits.remove("orange")
    return fruits

