#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that removes a http request.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    
    #Remove all links from the html page
    soup.findAll('a')
    
    #Write the html page to a file
    file = open("snirps.html", "w")
    file.write(soup.prettify())
    file.close()
    
    #Run the program
    
    

