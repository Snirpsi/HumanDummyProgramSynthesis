#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or converts a list of numbers. """    
    while True:
        words = input("Enter a list of words: ")
        numbers = input("Enter a list of numbers: ")
        
        if words and numbers:
            words = words.split()
            numbers = numbers.split()
            
            for word in words:
                if word in numbers:
                    numbers.remove(word)
            
            print(numbers)
            
        elif words and numbers:
            print("Invalid input. Try again.")
        else:
            print("Invalid input. Try again.")
            
