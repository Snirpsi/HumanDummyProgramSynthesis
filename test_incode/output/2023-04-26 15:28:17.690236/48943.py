#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and converts words. """    
    port = int(sys.argv[1])
    
    words = []
    
    while(True):
        words.append(input("Enter a word: "))
        
        if words[-1] == 'q':
            break
    
    print("Server listening on port %d" % port)
    
    words = [word.lower() for word in words]
    
    for word in words:
        word = word.strip()
        
        if word == 'q':
            break
        
        port = port + 1
        
        print("Converting %s to %s..." % (word, words[port]))
        
        word = words[port]
        
        word = word.lower()
        
        word = word.split()
        
        for word in word:
            print(word)
            
        print("Done.")
        
    print("\nBye!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    