from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    words = [tag for tag in soup.find_all()][550:600]
    title = [tag.h2.text.strip() for tag in words if tag.h2 is not None][0]
    description = [tag.text.strip() for tag in soup.find_all('div') if 'Build enterprise-ready' in tag.text][-1]
    image = [tag['src'].strip() for tag in soup.find_all('img', src=True) if 'dotd' in tag['src']][0]
    link = [tag['href'].strip() for tag in soup.find_all('a', href=True) if 'application-development' in tag['href']][-1]
    
    return Book(title=title, description=description, image=image, link=link)
    
    


print(get_book())