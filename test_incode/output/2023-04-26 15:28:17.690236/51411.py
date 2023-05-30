#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    import os
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from wordlist import Wordlist
    
    wordlist = Wordlist('wordlist.txt')
    
    wordlist.load()
    
    wordlist.display()
    
    wordlist.multiply(sys.argv[1])
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()
    
    wordlist.display()
    
    wordlist.save()
    
    wordlist.display()
    
    wordlist.delete()