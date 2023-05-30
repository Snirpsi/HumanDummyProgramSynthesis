#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that iterates over fruits.
    while True:
        print("Type 'quit' to quit.")
        fruir = input("Type a fruit: ")
        if fruir == "quit":
            break
        else:
            print(fruir)

