#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that calculates fruits.
    while True:
        fruits = fruirs
        fruits.append(input("Enter a fruit: "))
        print(fruits)
        #A break to exit the loop.
        if fruits[-1] == "apple":
            break
        #A continue to continue the loop.
        else:
            continue

