#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that enumerates a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        
        #Find the first h2 tag that contains the word "snirps".
        snirps = soup.find_all('h2', class_='snirps')
        
        #Print the text of the first h2 tag.
        print(snirps[0].text)
        
        #Wait for 10 seconds and then print again.
        time.sleep(10)

