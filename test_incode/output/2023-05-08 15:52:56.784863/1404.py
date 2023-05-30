#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that converts a http request.
    while True:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        
        #Get all links in the page
        anchors = soup.find_all('a')
        
        #For each link, get the href and save it to a file
        for a in anchors:
            href = a.get('href')
            urllib.request.urlretrieve(href, './' + href)
        
        #Wait for 5 seconds and then exit
        time.sleep(5)

