#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or prints all ports. """    
    while True:
        words = []
        ports = []
        
        ports.append(input("Enter a port number: "))
        
        while True:
            words.append(input("Enter a word: "))
            
            if words[-1] == 'q':
                break
            
            if words[-1] == 'q' and len(words) > 2:
                break
            
            if words[-1] == 'q' and len(words) == 2:
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isdigit():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isalpha():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isalnum():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isspace():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].islower():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isupper():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isdigit() and words[0].isalpha():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isdigit() and words[0].isalnum():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isspace():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].islower() and words[0].isupper():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isdigit() and words[0].isdigit() and words[0].isalnum():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isspace():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].islower() and words[0].isupper() and words[0].isalnum():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isdigit() and words[0].isdigit() and words[0].isdigit() and words[0].isalnum():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isspace():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].islower() and words[0].isupper() and words[0].isdigit() and words[0].isdigit() and words[0].isalnum():
                break
            
            if words[-1] == 'q' and len(words) == 1 and words[0].isdigit() and words[0].isdigit() and words[0].isdigit() and words[0].isdigit() and words[0].isalnum