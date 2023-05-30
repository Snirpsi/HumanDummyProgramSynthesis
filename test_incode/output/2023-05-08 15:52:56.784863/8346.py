#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that enumerates fruits.
    while True:
        print("Fruits:")
        for fruit in fruirs:
            print(fruit)
        print("\nEnter a fruit: ")
        fruit = input()
        if fruit == "quit":
            break
        else:
            fruirs.append(fruit)
    print("Done!")

