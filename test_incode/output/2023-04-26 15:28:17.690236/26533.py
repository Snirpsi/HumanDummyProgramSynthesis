#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words or calculates a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words = sys.argv[2:]
            
            for word in words:
                
                port = int(word)
                
                print(f"{word} -> {port}")
                
        else:
            
            port = sys.argv[1]
            
            print(f"{port} -> {port}")
            
    else:
        
        print("Usage: python3 ports.py words")
        
