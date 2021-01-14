from collections import Counter
from string import ascii_letters, digits
import bs4
import requests
import re

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    response = requests.get(url).text
    soup = bs4.BeautifulSoup(response, 'html.parser')
    emails = soup.findAll('div', class_='middle_info_noborder')
    for item in emails:
        item = re.findall(r'[A-Za-z]+\.[a-z]+\.?[a-z]+', item.text)
    
    return item
        


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()
    
    email_domains = [email.split('@')[1] for email in emails if email.split('@')[1]\
        not in set(common_domains)]
    
    return sorted(Counter(email_domains).items(),key=lambda x: x[1], reverse=True)


print(get_most_common_domains(["a@gmail.es", "b@googlemail.com", "c@somedomain.com",
      "d@somedomain.com", "e@somedomain.com", "f@hotmail.fr"]))