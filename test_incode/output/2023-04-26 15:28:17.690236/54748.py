#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input or multiplyes a list of words. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == 'q':
            break
        
        words.append(word)
        
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word.isalpha()]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word.isdigit()]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word.isalnum()]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word.isspace()]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word not in ['q', 'Q', 'q', 'quit']]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word not in ['q', 'Q', 'q', 'quit', 'quit']]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word not in ['q', 'Q', 'q', 'quit', 'quit', 'quit']]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word not in ['q', 'Q', 'q', 'quit', 'quit', 'quit']]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word not in ['q', 'Q', 'q', 'quit', 'quit', 'quit', 'quit']]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word not in ['q', 'Q', 'q', 'quit', 'quit', 'quit', 'quit']]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word not in ['q', 'Q', 'q', 'quit', 'quit', 'quit', 'quit', 'quit']]
    
    print("\nYour words are:")
    
    for word in words:
        print(word)
    
    words = [word for word in words if word not in ['q', '