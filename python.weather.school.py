import urllib.request
from bs4 import BeautifulSoup
from pprint import pprint

from urllib.request import Request, urlopen

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('http://httpbin.org/user-agent')
f = open('wunder-data.txt','w')

# Iterate through months and day
for m in range(1,13):
    for d in range(1,32):

        # Check if already gone through month
        if(m==2 and d>28):
            break
        elif(m in [4,6,9,11] and d>30):
            break

        # Open wunderground.com url
        timestamp = '2009-'+str(m)+"-"+str(d)
        print("getting data for "+timestamp)
        url = Request("https://www.wunderground.com/history/airport/KBUF/2009/"+str(m)+"/"+str(d)+"/DailyHistory.html?hdf=1", headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url).read()

        #Get temperature from page
        soup = BeautifulSoup(page)
        dayTemp = soup.findAll(attrs={"class":"wx-value"})[2].string

        # Format month for timestamp
        if len(str(m)) < 2:
            mStamp = '0' + str(m)
        else:
            mStamp = str(m)

        if len(str(d)) < 2:
            dStamp = '0' + str(d)
        else:
            dStamp = str(d)

        timestamp = '2009' + mStamp + dStamp

        f.write(timestamp + ',' + dayTemp + '\n')
f.close()