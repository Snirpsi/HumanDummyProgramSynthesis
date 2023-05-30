#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if number > 0:
            
            words = []
            
            for i in range(number):
                
                words.append(sys.argv[2])
                
            print(" ".join(words))
            
        else:
            
            print("No numbers given.")
            
    else:
        
        print("Usage: python wordlist.py <number> [word]")
        
