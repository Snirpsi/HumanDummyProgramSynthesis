#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    while True:
        try:
            list_to_ints(sys.argv[1])
        except ValueError as e:
            print(e)
            sys.exit(1)
        except IndexError:
            print('Usage: python list_to_ints.py <list>')
            sys.exit(1)
        except KeyboardInterrupt:
            print('\nBye!')
            sys.exit(1)

<|/ file ext=.py source=github |>