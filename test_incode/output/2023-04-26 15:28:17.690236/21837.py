#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or multiplyes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = [sys.argv[1].strip()]
    else:
        words = input("Enter a word: ")
    
    if len(words) == 0: 
        print("No words entered")
        sys.exit()
    
    words = [word.lower() for word in words.split()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit', 'exit', 'quit']]
    
    words = [word for word in words if word not in ['quit