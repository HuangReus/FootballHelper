from urllib.request import urlopen
from lxml import etree
from bs4 import BeautifulSoup

url="http://data.champdas.com/team/rank-12-2017.html"
try:
    html=urlopen(url)
except (HTTPError,URLError) as e:
    print(e)
"""
try:
    bsObj=BeautifulSoup(html.read(),'lxml')
except AttributeError as e:
    print(e)

for sibling in bsObj.find("table",{"id":"table1"}).tbody.tr.next_siblings:
    print(sibling)
"""
try:
    selector=etree.HTML(html.read().decode('utf-8'))
except:
    print("Exception!")

try:
    path='//table[@id="table1"]/tbody/tr'
    rank_index=selector.xpath(path)
except:
    print("Exception")

for each in rank_index:
    data=each.xpath('td')
    for j in range(0,len(data)):
        if(j==0):
            ranking=data[j].xpath('span/text()')
        elif j==1:
            club_name=data[j].xpath('a/text()')
        else:
            print(data[j].xpath('text()'))


