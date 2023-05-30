#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and converts words. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words.sort()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['help', 'h', 'help']]
