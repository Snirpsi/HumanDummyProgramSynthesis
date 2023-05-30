#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that enumerates a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        
        #Print the title of the page.
        print(soup.title)
        
        #Print the links of the page.
        for link in soup.find_all('a'):
            print(link.get('href'))
        
        #Print the content of the page.
        for content in soup.find_all('p'):
            print(content.text)
        
        #Pause for 5 seconds.
        time.sleep(5)

