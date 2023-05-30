#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from wordlist import WordList
    
    wordlist = WordList()
    
    wordlist.load_words()
    
    wordlist.print_words()
    
    wordlist.print_words_by_frequency()
    
    wordlist.print_words_with_frequency_in_range()
    
    wordlist.print_words_with_frequency_in_range_by_frequency()
    
    wordlist.print_words_with_frequency_in_range_by_frequency