#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words and converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python wordlist.py words.txt")
        exit()
    
    words = []
    for line in open(sys.argv[1]):
        words.append(line.strip())
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if len(word) > 1]
    
    words.sort()
    
    words = [word for word in words if len(word) > 2]
    
    words.sort()
    
    words = [word for word in words if len(word) > 3]
    
    words.sort()
    
    words = [word for word in words if len(word) > 4]
    
    words.sort()
    
    words = [word for word in words if len(word) > 5]
    
    words.sort()
    
    words = [word for word in words if len(word) > 6]
    
    words.sort()
    
    words = [word for word in words if len(word) > 7]
    
    words.sort()
    
    words = [word for word in words if len(word) > 8]
    
    words.sort()
    
    words = [word for word in words if len(word) > 9]
    
    words.sort()
    
    words = [word for word in words if len(word) > 10]
    
    words.sort()
    
    words = [word for word in words if len(word) > 11]
    
    words.sort()
    
    words = [word for word in words if len(word) > 12]
    
    words.sort()
    
    words = [word for word in words if len(word) > 13]
    
    words.sort()
    
    words = [word for word in words if len(word) > 14]
    
    words.sort()
    
    words = [word for word in words if len(word) > 15]
    
    words.sort()
    
    words = [word for word in words if len(word) > 16]
    
    words.sort()
    
    words = [word for word in words if len(word) > 17]
    
    words.sort()
    
    words = [word for word in words if len(word) > 18]
    
    words.sort()
    
    words = [word for word in words if len(word) > 19]
    
    words.sort()
    
    words = [word for word in words if len(word) > 20]
    
    words.sort()
    
    words = [word for word in words if len(word) > 21]
    
    words.sort()
    
