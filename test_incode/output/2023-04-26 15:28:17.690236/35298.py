#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words or multiplyes user input. """    
    
    wordlist = list()
    
    while True:
        try:
            wordlist.append(input("Enter a word: "))
        except:
            break
    
    wordlist = list(filter(None, wordlist))
    
    if len(wordlist) == 0:
        print("No words entered")
        
    else:
        print("\nMultiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
        for word in wordlist:
            print(word, "*", word, "=", word*word)
            
        print("\nThe multiplication of", len(wordlist), "words:")
