import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}
        self.response = requests.get(url = self.url, headers= self.user_agent).text
        self.soup = BeautifulSoup(self.response, 'lxml')

    def product_title(self): 
        title = self.soup.find('span', attrs={'id':'productTitle'})
        if title is  not None:
            return title.text.strip()
        else:
            return "No title found" 
    def product_price(self):
        price = self.soup.find('span', attrs={'class':'a-price-whole'})
        if price is not None:
            return price.text.strip()
        else:
            return "No price found"



device = PriceTracer(url='https://www.amazon.in/Samsung-Storage-Display-Charging-Security/dp/B0DFY3XCB6/ref=lp_4363159031_1_1?pf_rd_p=9e034799-55e2-4ab2-b0d0-eb42f95b2d05&pf_rd_r=TN2YD2VKHHAZ4EJZJWP3&sbo=9ZOMT9Jm0JH%2Ft%2BWi68iDSA%3D%3D')
print(device.product_title())
print(device.product_price())


samsung = PriceTracer(url='https://www.amazon.in/Samsung-Galaxy-Smartphone-Titanium-Storage/dp/B0CS5XW6TN/ref=lp_4363159031_1_2?pf_rd_p=9e034799-55e2-4ab2-b0d0-eb42f95b2d05&pf_rd_r=TN2YD2VKHHAZ4EJZJWP3&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D')
print(samsung.product_title())
print(samsung.product_price())