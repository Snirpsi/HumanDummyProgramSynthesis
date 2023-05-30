#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that prints fruits.
    while True:
        print("Fruits:")
        for fruit in fruirs:
            print(fruit)
        print("\nPress enter to exit")
        choice = input("\nEnter your choice: ")
        if choice == "exit":
            break
        else:
            fruirs.append(choice)

