#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    while True:
        fruits = input("Enter your favorite fruits: ").split()
        fruits = list(fruits)
        fruits.sort()
        print(fruits)
        time.sleep(1)
        
