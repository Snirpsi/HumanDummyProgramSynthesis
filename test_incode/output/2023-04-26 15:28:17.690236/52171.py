#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or removes numbers. """    
    while True:
        try:
            num = input("Enter a number: ")
            if num.isdigit():
                num = int(num)
                if num > 0:
                    num -= 1
                    while num > 0:
                        print(num, end=" ")
                        num 