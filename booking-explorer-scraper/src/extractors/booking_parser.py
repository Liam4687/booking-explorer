thon
import requests
from bs4 import BeautifulSoup

def parse_booking_data(search_query):
    url = f"https://www.booking.com/searchresults.html?ss={search_query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    hotels = soup.find_all('div', class_='sr_property_block')
    
    hotel_data = []
    for hotel in hotels:
        data = {
            "name": hotel.find('span', class_='sr-hotel__name').text.strip(),
            "price": hotel.find('div', class_='bui-price-display__value').text.strip(),
            "rating": hotel.find('div', class_='bui-review-score__badge').text.strip()
        }
        hotel_data.append(data)
    
    return hotel_data