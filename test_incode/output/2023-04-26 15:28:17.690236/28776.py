#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 add_word.py <word>")
        exit(1)
    
    word = sys.argv[1]
    
    print("Adding word: " + word)
    
    wordlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    wordlist.insert(0, word)
    
    print("Wordlist: " + wordlist)
    
    wordlist.sort()
    
    print("Sorted wordlist: " + wordlist)
    
    wordlist.append("z")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("e")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("j")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("k")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("l")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("m")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("n")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("o")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("p")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("q")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("r")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("s")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("t")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("u")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("v")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("w")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("x")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("y")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("z")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("a")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("b")
    
    print("Wordlist: " + wordlist)
    
    wordlist.append("c")
    
    print("Wordlist: " + 