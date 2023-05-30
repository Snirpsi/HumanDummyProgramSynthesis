#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        print("Type 'quit' to quit.")
        fruir = input("Type a fruit: ")
        if fruir == "quit":
            break
        else:
            fruirs.append(fruir)
    print("The fruits are", fruirs)

