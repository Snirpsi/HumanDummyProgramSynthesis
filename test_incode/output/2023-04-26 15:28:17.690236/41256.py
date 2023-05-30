#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and iterates over numbers. """    
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: %s <word> <numbers>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    numbers = sys.argv[2].split()
    
    for number in numbers:
        number = int(number)
        
        for word in words:
            word = word.strip()
            
            if word:
                word = word.lower()
                
                if word.isdigit():
                    number = number * number
                else:
                    number = number * int(word)
                
                print("%d * %d = %d" % (number, word, number))
                
