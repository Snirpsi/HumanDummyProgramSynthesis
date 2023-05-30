#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits and calculates a list of words. """    
    while True:
        fruit = input("Enter a fruit: ")
        fruits.append(fruit)
        
        words = fruit.split()
        
        for word in words:
            if word in fruits:
                fruits.remove(word)
        
        print("The fruits of your choice are:")
        for fruit in fruits:
            print(fruit)
        
        print("The words of your choice are:")
        for word in words:
            print(word)
        
        print("Do you want to continue (y/n)? ")
        
        answer = input("