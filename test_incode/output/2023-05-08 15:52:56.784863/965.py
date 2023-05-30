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
        if answer > 100 or answer < 0:
            print("Invalid input. Try again.")
            continue
        break
    print(answer)

