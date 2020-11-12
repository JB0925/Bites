from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    if start < 0:
        start = 0
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text = list(func(*args, **kwargs))
            try:
                for i in range(start, end):
                    text[i] = DOT
            except IndexError:
                pass
            return ''.join(text)
        return wrapper
    return decorate


@strip_range(0,3)
def gen_text(s):
    return s


print(gen_text('Welcome to PyBites'))

