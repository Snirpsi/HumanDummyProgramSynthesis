#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from wordlist import WordList
    
    wordlist = WordList()
    
    wordlist.load_wordlist()
    
    wordlist.print_wordlist()
    
    wordlist.print_wordlist_with_scores()
    
    wordlist.print_wordlist_with_scores(with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True)
    
    wordlist.print_wordlist_with_scores(with_scores=True, with_scores=True, with_scores=True, with_scores=True, with_scores=True, 