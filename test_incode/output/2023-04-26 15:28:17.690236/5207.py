#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers or calculates words. """    
    
    numbers = []
    words = []
    
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        
        try:
            number = int(number)
        except ValueError:
            print("Invalid number")
            continue
        
        numbers.append(number)
        
        word = input("Enter a word: ")
        if word == "":
            break
        
        try:
            words.append(word)
        except ValueError:
            print("Invalid word")
            continue
        
    print("Numbers: ", numbers)
    print("Words: ", words)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    