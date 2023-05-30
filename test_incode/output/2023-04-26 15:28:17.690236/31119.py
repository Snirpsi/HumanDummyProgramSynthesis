#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word not in ['and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', 'of', 'the', 'to', 'from', 'and', 'or', 'not', 'the', '