#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words = sys.argv[2:]
            
            words = [word.strip() for word in words]
            
            words = [word.lower() for word in words]
            
            words = [word for word in words if word.isalpha()]
            
            words = [word for word in words if word.isdigit()]
            
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
            
            words = [word for word in words if word not in ['quit', 'exit', 'quit']]
            
            words = [word for word in words if word not in ['quit', 'exit', 'quit']]
            
            words = [word for word in words if word not in ['quit', 'exit', 'quit']]
            
            words = [word for word in words if word 