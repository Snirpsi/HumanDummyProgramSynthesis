#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or prints numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python wordlist.py <words>")
        sys.exit()
    
    words = [word.strip() for word in sys.argv[1].split(",")]
    
    for word in words:
        word = word.strip()
        
        if word == "":
            continue
        
        if word[0].isdigit():
            print(int(word))
        else:
            print(word)
