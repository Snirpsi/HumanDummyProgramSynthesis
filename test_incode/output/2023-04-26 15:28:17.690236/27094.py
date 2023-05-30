#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    import sys
    import os
    import webbrowser
    from optparse import OptionParser
    
    parser = OptionParser()
    parser.add_option("-d", "--directory", dest="directory", help="directory to convert to", metavar="DIRECTORY")
    parser.add_option("-w", "--word", dest="word", help="word for conversion", metavar="WORD")
    
    (options, args) = parser.parse_args()
    
    directory = options.directory
    word = options.word
    
    if directory is None:
        parser.error("directory not specified")
    
    if word is None:
        parser.error("word not specified")
    
    directory = os.path.abspath(directory)
    
    words = [os.path.join(directory, word) for word in os.listdir(directory) if word.endswith(".txt")]
    
    if len(words) == 0:
        parser.error("no .txt files found")
    
    webbrowser.open_new_tab(words[0])
    
    
