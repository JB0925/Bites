content = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    tail_list = []
    filepath = filepath.split('\n')
    for index,line in enumerate(filepath, 1):
        if len(filepath) - index < n:
            tail_list.append(line)
        else:
            continue
    return tail_list
        



print(tail(content,1))