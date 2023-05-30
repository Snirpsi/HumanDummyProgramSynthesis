#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        fruits.append(fruit)
        print("Added " + fruit + "!")
        time.sleep(1)
        
# vim:ts=4:sw=4: