#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        print("\nFruit Adder")
        print("=========================")
        print("\nEnter a fruit: ")
        fruit = input()
        if fruit in fruirs:
            fruirs.remove(fruit)
        else:
            print("\nInvalid fruit")
            print("=========================")
        print("\nFruit Added")
        print("=========================")
        print("\nFruit List: ")
        print(fruirs)
        print("\nPress Enter to exit")
        input()

