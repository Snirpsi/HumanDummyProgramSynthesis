#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that requests numbers.
    #It will print them out in reverse order.
    #It will also ask the user if they want to quit.
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers.reverse()
    print(numbers)
    quit = input("Do you want to quit? [y/n]")
    if quit == "y":
        print("Goodbye!")
    else:
        print("Goodbye!")

