#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or adds a list of words. """    
    while True:
        port = input("Enter a port number: ")
        words = []
        
        # Store words in a list
        while True:
            word = input("Enter a word: ")
            words.append(word)
            
            # Check if word is valid
            if not word.isalpha():
                print("Invalid word.")
                continue
            
            # Check if word is unique
            if word not in words:
                print("Word already in list")
                continue
            
            break
        
        # Store words in a list
        words = list(set(words))
        
        # Print words and port
        print("Words:", words)
        print("Port:", port)
        
        # Wait for user to enter another port
        while True:
            port = input("Enter another port number: ")
            
            # Check if port is valid
            if not port.isdigit():
                print("Invalid port")
                continue
            
            # Check if port is unique
            if port not in range(10000, 65535):
                print("Port already in use")
                continue
            
            break
        
        # Print words and port
        print("Words:", words)
        print("Port:", port)
        
        # Wait for user to enter another word
        while True:
            word = input("Enter another word: ")
            
            # Check if word is valid
            if not word.isalpha():
                print("Invalid word")
                continue
            
            # Check if word is unique
            if word not in words:
                print("Word already in list")
                continue
            
            break
        
        # Print words and port
        print("Words:", words)
        print("Port:", port)
        
        # Wait for user to enter another word
        while True:
            word = input("Enter another word: ")
            
            # Check if word is valid
            if not word.isalpha():
                print("Invalid word")
                continue
            
            # Check if word is unique
            if word not in words:
                print("Word already in list")
                continue
            
            break
        
        # Print words and port
        print("Words:", words)
        print("Port:", port)
        
        # Wait for user to enter another word
        while True:
            word = input("Enter another word: ")
            
            # Check if word is valid
            if not word.isalpha():
                print("Invalid word")
                continue
            
            # Check if word is unique
            if word not in words:
                print("Word already in list")
                continue
            
            break
        
        # Print words and port
        print("Words:", words)
        print("Port:", port)
        
        # Wait for user to enter another word
        while True:
            word = input("Enter another word: ")
            
            # Check if word is valid
            if not word.isalpha():
                print("Invalid word")