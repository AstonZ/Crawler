from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

# regular condition
# 1. start with /wiki/
# 2. not include :
regular = "^(/wiki/)((?!:).)*$"

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html)
for link in bsObj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile(regular)):
    if 'href' in link.attrs:
        print(link.attrs['href'])
