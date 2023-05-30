#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that calculates a http request.
    while True:
        req = requests.get(url)
        req.raise_for_status()
        soup = BeautifulSoup(req.text, 'html.parser')
        
        #Get all links in the page
        anchors = soup.find_all('a')
        
        #For each link, get the href and save it to a list.
        for a in anchors:
            href = a.get('href')
            
            #If the href is valid, save the href to a list.
            if href is not None:
                hrefs.append(href)
        
        #Print the list of hrefs.
        print(hrefs)
        
        #Pause for 5 seconds.
        time.sleep(5)

