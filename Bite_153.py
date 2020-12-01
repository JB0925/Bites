def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    transactions = [int(str(t).split('.')[0]) for t in transactions]
    
    if up:
        return [t + 1 for t in transactions]
    
    return [t if t>= 0 else t - 1 for t in transactions]




transactions1 = [2.05, 3.55, 4.50, 10.76, 100.25]
transactions2 = [1.55, 9.17, 5.67, 6.77, 2.33, -2.05]

print(round_up_or_down(transactions2,up=True))