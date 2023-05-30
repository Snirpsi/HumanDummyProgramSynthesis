#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that converts a http request.
    while True:
        req = requests.get(url)
        req.raise_for_status()
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        
        #Get all links in the page
        links = soup.find_all('a')
        
        #For each link, get the url and save it to a file
        for link in links:
            url = link.get('href')
            
            #Save the url to a file
            save_file(url)
            
        #Wait for a second
        time.sleep(1)

