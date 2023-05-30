#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that enumerates fruits.
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "quit":
            break
        else:
            print(fruirs[fruit.index(fruit)+1]) # get the next fruit index
            #print(fruit) # print the fruit name

