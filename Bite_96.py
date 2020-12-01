import requests

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    lines = len(file_.splitlines())
    words = len(file_.split())
    characters = len(file_)
    return f'{lines}\t{words}\t{characters} {file_}'


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))

lines = ['Hello world',
         'Keep calm and code in Python',
         'Have a nice weekend']

url = 'https://bites-data.s3.us-east-2.amazonaws.com/driving.py'

response = requests.get(url)
content = response.text

# print(wc(content))