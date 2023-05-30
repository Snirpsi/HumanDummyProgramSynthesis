#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers and calculates words. """    
    
    number = int(input("Enter a number: "))
    
    word = ""
    
    if number > 0 and number <= 10:
        word = "One"
    elif number > 10 and number <= 20:
        word = "Two"
    elif number > 20 and number <= 30:
        word = "Three"
    elif number > 30 and number <= 40:
        word = "Four"
    elif number > 40 and number <= 50:
        word = "Five"
    elif number > 50 and number <= 60:
        word = "Six"
    elif number > 60 and number <= 70:
        word = "Seven"
    elif number > 70 and number <= 80:
        word = "Eight"
    elif number > 80 and number <= 90:
        word = "Nine"
    elif number > 90:
        word = "Ten"
        
    print(word)
    
