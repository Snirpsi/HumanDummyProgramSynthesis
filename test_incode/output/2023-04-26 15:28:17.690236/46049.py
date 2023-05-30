#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or opens user input. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number < 1:
                print('Invalid number')
            else:
                print('You entered ' + str(number))
        except ValueError:
            print('Invalid number')
        except EOFError:
            print('Bye')
            break
        except KeyboardInterrupt:
            print('Bye')
            break
        else:
            print('You entered ' + str(number))
            
