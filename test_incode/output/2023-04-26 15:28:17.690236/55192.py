#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or removes numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Invalid number')
            continue
        else:
            if number > 0 and number < 10:
                print(number)
            elif number > 10 and number < 100:
                print(number - 10)
            elif number > 100 and number < 1000:
                print(number - 100)
            elif number > 1000 and number < 10000:
                print(number - 1000)
            elif number > 10000 and number < 100000:
                print(number - 10000)
            elif number > 100000 and number < 1000000:
                print(number - 100000)
            elif number > 1000000 and number < 10000000:
                print(number - 1000000)
            elif number > 10000000 and number < 100000000:
                print(number - 10000000)
            elif number > 100000000 and number < 10000000000:
                print(number - 100000000)
            elif number > 10000000000 and number < 100000000000:
                print(number - 10000000000)
            elif number > 100000000000 and number < 1000000000000:
                print(number - 100000000000)
            elif number > 1000000000000 and number < 1000000000000:
                print(number - 1000000000000)
            elif number > 10000000000000 and number < 100000000000000:
                print(number - 1000000000000)
            elif number > 100000000000000 and number < 1000000000000000:
                print(number - 100000000000000)
            elif number > 1000000000000000 and number < 10000000000000000:
                print(number - 100000000000000)
            elif number > 10000000000000000 and number < 100000000000000000:
                print(number - 10000000000000000)
            elif number > 100000000000000000 and number < 1000000000000000000:
                print(number - 100000000000000000)
            elif number > 1000000000000000000 and number < 10000000000000000000:
                print(number - 1000000000000000000)
            elif number > 10000000000000000000 and number < 100000000000000000000:
                print(number - 10000000000000000000)
            elif number > 100000000000000000000 and number < 100000000000000000000:
                print(number - 100000000000000000000)
            elif number > 1000000000000000000000 and number < 100000000000000000000:
                print(number - 100000000000000000000)
            elif number > 10000000000000000000000 and number < 100000000000000000000000:
                print(number - 100000000000000000000)
            elif number > 100000000000000000000000 and number < 1000000000000000000000000:
                print(number - 100000000000000000000)
            elif number > 1000000000000000000000000 and number < 10000000000000000000000000:
                print(number - 1000000000000000000000000)
            elif number > 10000000000000000000000000 and number < 100000000000000000000000000:
                print(number - 