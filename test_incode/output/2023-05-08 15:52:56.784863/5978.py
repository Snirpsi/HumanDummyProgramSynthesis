#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that converts user input.
    while True:
        answer = input("Enter a number: ")
        try:
            answer = int(answer)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        if answer < 0:
            print("Negative numbers are not allowed. Please try again.")
            continue
        if answer > 10:
            print("Maximum 10 numbers are not allowed. Please try again.")
            continue
        break

