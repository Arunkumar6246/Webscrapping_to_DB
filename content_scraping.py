"""
Scrapping the data  from website 

"""

import requests
from bs4 import BeautifulSoup
import WS_Db  as w

url="https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&bedrooms=11701,11702&cityName=Coimbatore&Locality=72106&page=2&groupstart=9&offset=2&maxOffset=13&sortBy=premiumRecent&postedSince=-1&isNRI=N"
r=requests.get(url)
c=r.content

soup=BeautifulSoup(c,'html.parser')

con=soup.find_all('div',{'class':'mb-srp__list'})

for item in con:
    
    Title=item.find('h2',{'class','mb-srp__card--title'}).text
    Ad_by=item.find('div',{'class','mb-srp__card__ads--name'}).text
    try:
        offers=item.find('div',{'class','mb-srp__card__offer'}).text
    except:
        offers=None
    
    rate=item.find('div',{'class','mb-srp__card__price--amount'}).text
    try:
        per_sqft=item.find('div',{'class','mb-srp__card__price--size'}).text.replace('₹','').replace(' per sqft','')
    except:
        per_sqft=None
    
    w.insert(Title,Ad_by,offers,rate,per_sqft)
    
    