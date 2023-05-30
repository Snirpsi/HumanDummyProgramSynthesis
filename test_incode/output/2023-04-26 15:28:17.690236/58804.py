#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and opens a list of numbers. """    
    
    words = []
    numbers = []
    
    while True:
        word = input("Enter a word: ")
        numbers.append(int(input("Enter a number: ")))
        words.append(word)
        
        if word in words:
            print("Found it!")
            break
        else:
            print("Sorry, I didn't find that.")
            
    numbers_str = " ".join(str(n) for n in numbers)
    
    print("The numbers are:", numbers_str)
    
