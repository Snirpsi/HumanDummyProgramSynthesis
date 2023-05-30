#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or adds user input. """    
    while True:
        try:
            num = input("Enter a number: ")
            if num.isdigit():
                num = int(num)
                print(num)
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
        except EOFError:
            print("Bye")
            break

<|/ file source=github dstars=0 |>