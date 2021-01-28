import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def get_html(url):
    return requests.get(url).text


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    questions = [question.text for question in\
        soup.find_all('a', class_='question-hyperlink')][:50]
    votes = [vote.text for vote in\
        soup.find_all('span', class_='vote-count-post')]
    views = [view.text.replace('\r\n', '').replace(' views', '').strip() for view in\
        soup.find_all('div', class_='views')]
    
    top_questions = list(zip(questions, votes, views))
    top_questions = [(t[0], int(t[1])) for t in top_questions if 'm' in t[2]]
    return sorted(top_questions, key=lambda x: x[1], reverse=True)

    
    
    
    



print(top_python_questions())