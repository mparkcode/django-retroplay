
from bs4 import BeautifulSoup
import requests
from .models import Game
base_urls=[
    'https://www.consolemad.co.uk/product-category/microsoft/xbox/uk-xbox-games/'
    ]

count = 0
      
for base_url in base_urls:
      
    url = base_url
    
    while url:
        url_list = url.split('/')
        brand = url_list[4]
        console = url_list[5]
        
        
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        
        pages=[]
        for ul in soup.find_all('ul', {'class': 'page-numbers'}):
            for li in ul.find_all('li'):
                for page_num in li.contents:
                    if page_num.text == '←' or page_num.text == '→':
                        continue
                    else:
                        pages.append(page_num.text)
        
        if soup.find('span', class_="current"):
            current_page = soup.find('span', class_="current").text
        else:
            current_page = None
        
        
        for product in soup.find_all('div', class_="entry-product"):
            
            picture_link = product.find('div', class_="entry-featured").a.img['src']
            # print(picture_link)
            # print(brand)
            # print(model)
            
            title = product.find('div', class_="entry-wrap").header.h3.a.text
            # print(title)
            
            price = product.find('div', class_="entry-wrap").header.span.span.text
            price = float(price[1:])
            # print(price)
            
            # print("--------------------------------")
            
            game = Game(title=title, price=price, brand=brand, console=console)
            game.save()
            print(title + "saved to db")
            
            count += 1
        if current_page and current_page != pages[-1]:
            next_page = int(current_page) + 1
            url = base_url + "page/{}/".format(next_page)
        else:
            url = None

print("Total Games: " + str(count))
   