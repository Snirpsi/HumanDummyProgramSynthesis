#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or adds fruits. """    
    while True:
        number = input("Enter a number: ")
        if number == 'quit':
            break
        else:
            number = int(number)
            if number % 2 == 0:
                print("Fruit added")
            else:
                print("Fruit converted")
                
