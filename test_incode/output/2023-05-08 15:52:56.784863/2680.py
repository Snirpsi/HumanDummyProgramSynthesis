#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        
        #Print the html of the page.
        print(soup.prettify())
        
        #Print the text of the page.
        print(soup.text)
        
        #Print the links of the page.
        for link in soup.find_all('a'):
            print(link.get('href'))
        
        #Wait a little while before continuing.
        time.sleep(5)

