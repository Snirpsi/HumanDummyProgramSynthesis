#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    # Open a word document
    doc = word.Document('word/document.docx')
    
    # Open a table of contents
    table = doc.TableOfContents()
    
    # Open a paragraph
    paragraph = doc.Paragraph('A paragraph')
    
    # Open a table
    table = doc.Table('A table')
    
    # Close the document
    doc.Close()
    
    # Close the table
    table.Close()
    
    # Close the paragraph
    paragraph.Close()
    
    # Close the table