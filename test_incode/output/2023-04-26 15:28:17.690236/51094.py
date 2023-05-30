#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        print('You have {} fruits.'.format(len(fruits)))
        print('Pick a fruit:')
        fruit = input()
        if fruit not in fruits:
            print('That fruit does not exist!')
        else:
            print('You picked {}'.format(fruit))
            print('You now have {} apples.'.format(len([x for x in fruits if x == fruit])))
            print('Pick a new fruit:')
            fruit = input()
            if fruit not in fruits:
                print('That fruit does not exist!')
            else:
                print('You picked {}'.format(fruit))
                print('You now have {} apples.'.format(len([x for x in fruits if x == fruit])))
                print('Pick a new fruit:')
                fruit = input()
                if fruit not in fruits:
                    print('That fruit does not exist!')
                else:
                    print('You picked {}'.format(fruit))
                    print('You now have {} apples.'.format(len([x for x in fruits if x == fruit])))
                    print('Pick a new fruit:')
                    fruit = input()
                    if fruit not in fruits:
                        print('That fruit does not exist!')
                    else:
                        print('You picked {}'.format(fruit))
                        print('You now have {} apples.'.format(len([x for x in fruits if x == fruit])))
                        print('Pick a new fruit:')
                        fruit = input()
                        if fruit not in fruits:
                            print('That fruit does not exist!')
                        else:
                            print('You picked {}'.format(fruit))
                            print('You now have {} apples.'.format(len([x for x in fruits if x == fruit])))
                            print('Pick a new fruit:')
                            fruit = input()
                            if fruit not in fruits:
                                print('That fruit does not exist!')
                            else:
                                print('You picked {}'.format(fruit))
                                print('You now have {} apples.'.format(len([x for x in fruits if x == fruit])))
                                print('Pick a new fruit:')
                                fruit = input()
                                if fruit not in fruits:
                                    print('That fruit does not exist!')
                                else:
                                    print('You picked {}'.format(fruit))
                                    print('You now have {} apples.'.format(len([x for x in fruits if x == fruit])))
                                    print('Pick a new fruit:')
                                    fruit = input()
                                    if fruit not in fruits:
                                        print('That fruit does not exist!')
                                    else:
                                        print('You picked {}'.format(fruit))
                                        print('You now have {} apples.'.format(len([x for x in fruits if x == fruit])))
                                        print('Pick a new fruit:')
                                        fruit = input()
                                        if fruit not in fruits:
                                            print('That fru