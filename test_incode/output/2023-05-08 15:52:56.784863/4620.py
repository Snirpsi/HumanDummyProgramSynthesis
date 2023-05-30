#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that iterates over user input.
    while True:
        answer = input("Enter a number: ")
        try:
            answer = int(answer)
        except ValueError:
            print("Invalid input.")
            continue
        if answer < 0:
            print("Negative number.")
            continue
        if answer > 0:
            print("Positive number.")
            continue
        break

