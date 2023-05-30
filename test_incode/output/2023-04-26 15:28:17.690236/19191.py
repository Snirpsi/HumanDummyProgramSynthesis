#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers or opens words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print(number)
        else:
            word = input("Enter a word: ")
            
            if word != "":
                print(word)
            else:
                print("No word entered")
    else:
        print("No number entered")
    
