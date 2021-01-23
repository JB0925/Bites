from pathlib import Path
from urllib.request import urlretrieve
from operator import itemgetter
from bs4 import BeautifulSoup

url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "best-programming-books.html")
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """
    def __init__(self, title, author, year, rank, rating):
        self.title = title
        self.author = author
        self.year = year
        self.rank = rank
        self.rating = rating

    
    def __str__(self):
        self.rank = str(self.rank).zfill(3)
        self.rating = float(self.rating)
        
        if ',' not in self.author:
            self.author = self.author.split()[-1] + ', ' + ' '.join(self.author.split()[0:-1])
            return f'''[{self.rank}] {self.title} ({self.year})
      {self.author} {self.rating}'''
        else:
            #self.author = self.author.split()[-1] + ', ' + ''.join(self.author.split()[0:-1])
            return f'''[{self.rank}] {self.title} ({self.year})
      {self.author} {self.rating}'''


def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    if year:
        books = [book for book in books if book.year >= year]
    for i in range(limit):
        try:
            print(books[i])
        except Exception:
            pass
        
    
    
    

def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    book_info = []

    soup = _get_soup(html_file)
    authors = [author.text.replace(' (You?)', '') for author in soup.find_all('h3', class_='authors')]
    ratings = [float(r.text) if len(r.text) > 1 else int(r.text) for r in soup.find_all('span', class_='our-rating')]
    titles = [title.text for title in soup.find_all('h2', class_='main')]
    ranks = [i for i in range(1, 101)]
    dates = [int(x.text.split('| ')[1].replace(' ', '')) if len(x.text.split('| ')) == 3 else 2020 for x in soup.find_all('div', class_='subtitle')]
    book_info = [Book(titles[i], authors[i], dates[i], ranks[i], ratings[i]) for i in range(len(ranks)) if\
                 authors[i] != 'Unknown' and dates[i] != 2020 and 'python' in titles[i].lower()]
    
    book_info = sorted(book_info, key=lambda x: (-x.rating, x.year, x.title.lower(), x.author.split()[1].lower()))
    for idx, book in enumerate(book_info, start=1):
        book.rank = str(idx)
        book.author = book.author.split()[-1] + ', ' + ' '.join(book.author.split()[0:-1])
    
    return book_info

    
    
    
    


def main():
    books = load_data()
    display_books(books, limit=1000, year=None)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""
