import requests
import json

YOUR_KEY = 'IiAw3whect7j4c7RZFoGVoKGAWPAWCJf'
DEFAULT_LIST = 'hardcover-nonfiction'

URL_NON_FICTION = (f'https://api.nytimes.com/svc/books/v3/lists/current/'
                   f'{DEFAULT_LIST}.json?api-key={YOUR_KEY}')
URL_FICTION = URL_NON_FICTION.replace('nonfiction', 'fiction')


def get_best_seller_titles(url=URL_NON_FICTION):
    """Use the NY Times Books API endpoint above to get the titles that are
       on the best seller list for the longest time.

       Return a list of (title, weeks_on_list) tuples, e.g. for the nonfiction:

       [('BETWEEN THE WORLD AND ME', 86),
        ('EDUCATED', 79),
        ('BECOMING', 41),
        ('THE SECOND MOUNTAIN', 18),
         ... 11 more ...
       ]

       Dev docs: https://developer.nytimes.com/docs/books-product/1/overview
    """
    all_books = requests.get(url).json()
    book_info = all_books['results']['books']
    book_info = [(row['title'], row['weeks_on_list']) for row in book_info]
    return sorted(book_info, key=lambda x: x[1], reverse=True)
    


if __name__ == '__main__':
    ret = get_best_seller_titles()
    print(ret)
