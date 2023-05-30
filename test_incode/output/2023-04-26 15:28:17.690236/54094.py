#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers and returns words. """    
    while True:
        num = input("Enter a number: ")
        if num == "q":
            break
        num = float(num)
        word = ""
        while num > 0:
            word = word + str(num % 10)
            num /= 10
        print(word)

<|/ file filename=