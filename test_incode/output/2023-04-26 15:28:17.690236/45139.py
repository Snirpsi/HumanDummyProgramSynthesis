#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or iterates over numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words|numbers]" % sys.argv[0])
        sys.exit(0)
    
    words = 0
    numbers = 0
    
    if sys.argv[1] == "words":
        words = 1
    elif sys.argv[1] == "numbers":
        numbers = 1
    else:
        print("Usage: %s [words|numbers]" % sys.argv[0])
        sys.exit(0)
    
    
    if words == 1:
        numbers = input("Enter a number: ")
        numbers = numbers.strip()
        
        if numbers:
            numbers = numbers.split()
            
            for number in numbers:
                number = number.strip()
                
                if number:
                    number = number.split()
                    
                    for number in number:
                        number = number.strip()
                        
                        if number:
                            number = number.split()
                            
                            print(number)
                            
        else:
            print("No numbers given.")
            
    elif numbers == 1:
        words = input("Enter a word: ")
        words = words.strip()
        
        if words:
            words = words.split()
            
            for word in words:
                word = word.strip()
                
                if word:
                    word = word.split()
                    
                    for word in word:
                        word = word.strip()
                        
                        if word:
                            word = word.split()
                            
                            print(word)
                            
        else:
            print("No words given.")
            
    else:
        print("Usage: %s [words|numbers]" % sys.argv[0])
        sys.exit(0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    