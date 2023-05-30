#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        filename = sys.argv[1]
        
        try:
            
            with open(filename) as file:
                
                text = file.read()
                
                text = text.replace("\n", "").replace("\t", "")
                
                with open(filename, "w") as file:
                    
                    file.write(text)
                    
        except FileNotFoundError:
            
            print("File not found")
            
        else:
            
            print("File successfully written")
            
    else:
        
        print("No filename given")
        
