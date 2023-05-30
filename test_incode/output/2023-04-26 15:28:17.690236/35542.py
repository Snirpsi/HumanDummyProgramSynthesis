#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or calculates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
    else:
        wordlist = input("Enter words to add: ")
    
    wordlist = wordlist.split()
    
    wordlist.sort()
    
    numbers = []
    
    for word in wordlist:
        try:
            number = int(word)
            numbers.append(number)
        except ValueError:
            print("Invalid number")
    
    numbers.sort()
    
    for number in numbers:
        print(number)
    
