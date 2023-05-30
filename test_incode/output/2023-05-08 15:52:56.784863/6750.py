#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that calculates user input.
    while True:
        answer = input("Enter a number: ")
        try:
            answer = int(answer)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        if answer > 100 or answer < 0:
            print("Invalid input. Please try again.")
            continue
        break
    print(answer)

