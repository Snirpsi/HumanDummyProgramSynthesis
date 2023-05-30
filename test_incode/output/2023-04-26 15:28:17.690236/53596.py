#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits and enumerates fruits. """    
    while True:
        fruits = input('Enter a fruit or enter q to quit: ')
        if fruits == 'q':
            break
        else:
            fruits = fruits.lower()
            if fruits == 'apple':
                apple = input('Enter a fruit or enter q to quit: ')
                if apple == 'q':
                    break
                else:
                    apple = apple.lower()
                    if apple == 'banana':
                        banana = input('Enter a fruit or enter q to quit: ')
                        if banana == 'q':
                            break
                        else:
                            banana = banana.lower()
                            if banana == 'orange':
                                orange = input('Enter a fruit or enter q to quit: ')
                                if orange == 'q':
                                    break
                                else:
                                    orange = orange.lower()
                                    if orange == 'mango':
                                        mango = input('Enter a fruit or enter q to quit: ')
                                        if mango == 'q':
                                            break
                                        else:
                                            mango = mango.lower()
                                            if mango == 'kiwi':
                                                kiwi = input('Enter a fruit or enter q to quit: ')
                                                if kiwi 