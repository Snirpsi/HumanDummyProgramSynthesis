#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that converts user input.
    while True:
        answer = input("Enter a number: ")
        try:
            answer = int(answer)
        except ValueError:
            print("Invalid input. Try again.")
            continue
        else:
            break
    #The program ends when you enter a number that isn't a number.
    if answer == "":
        print("Invalid input. Try again.")
    else:
        print("The number you entered is", answer)

