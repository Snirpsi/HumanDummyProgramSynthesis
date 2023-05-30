#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        try:
            answer = input('Enter your choice: ')
            if answer == 'quit':
                break
            elif answer == 'exit':
                exit()
            else:
                print('You entered', answer)
        except KeyboardInterrupt:
            print('Bye!')
            break
