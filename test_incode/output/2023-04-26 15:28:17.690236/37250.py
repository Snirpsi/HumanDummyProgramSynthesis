#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words or removes a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = input("Enter the file name: ")
        
    file = open(file, 'r')
    
    words = file.read().splitlines()
    
    file.close()
    
    words = list(set(words))
    
    words.sort()
    
    file = open("wordlist.txt", "w")
    
    for word in words:
        file.write(word + "\n")
    
    file.close()
    
    file = open("wordlist.txt", "r")
    
    wordlist = file.read().splitlines()
    
    file.close()
    
    file = open("wordlist.txt", "w")
    
    for word in wordlist:
        file.write(word + "\n")
    
    file.close()
    
    file = open("wordlist.txt", "r")
    
    wordlist = file.read().splitlines()
    
    file.close()
    
    file = open("wordlist.txt", "w")
    
    for word in wordlist:
        file.write(word + "\n")
    
    file.close()
    
    file = open("wordlist.txt", "r")
    
    wordlist = file.read().splitlines()
    
    file.close()
    
    file = open("wordlist.txt", "w")
    
    for word in wordlist:
        file.write(word + "\n")
    
    file.close()
    
    file = open("wordlist.txt", "r")
    
    wordlist = file.read().splitlines()
    
    file.close()
    
    file = open("wordlist.txt", "w")
    
    for word in wordlist:
        file.write(word + "\n")
    
    file.close()
    
    file = open("wordlist.txt", "r")
    
    wordlist = file.read().splitlines()
    
    file.close()
    
    file = open("wordlist.txt", "w")
    
    for word in wordlist:
        file.write(word + "\n")
    
    file.close()
    
    file = open("wordlist.txt", "r")
    
    wordlist = file.read().splitlines()
    
    file.close()
    
    file = open("wordlist.txt", "w")
    
    for word in wordlist:
        file.write(word + "\n")
    
    file.close()
    
    file = open("wordlist.txt", "r")
    
    wordlist = file.read().splitlines()
    
    file.close()
    
    file = open("wordlist.txt", "w")
    
    for word in wordlist:
        file.write(word + "\n")
    
    file.close()
    
    file = open("wordlist.txt", "r")
    
    wordlist = file.read().splitlines()
    
    file.close()
    
    file = open("wordlist.txt", "w")
    
    for word in wordlist:
        