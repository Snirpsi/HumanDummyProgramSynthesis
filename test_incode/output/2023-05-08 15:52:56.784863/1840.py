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
        
        #Print the text of the page.
        for paragraph in soup.find_all('p'):
            print(paragraph.text)
        
        #Pause for a few seconds.
        time.sleep(3)

