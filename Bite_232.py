# https://pkgstore.datahub.io/core/gold-prices/annual_csv/data/343f626dd4f7bae813cfaac23fccd1bc/annual_csv.csv
gold_prices = """
1980-12,596.712 1981-12,410.119 1982-12,444.776 1983-12,388.060 1984-12,319.622
1985-12,321.985 1986-12,391.595 1987-12,487.079 1988-12,419.248 1989-12,409.655
"""
# 1990-12,378.161 1991-12,361.875 1992-12,334.657 1993-12,383.243 1994-12,379.480
# 1995-12,387.445 1996-12,369.338 1997-12,288.776 1998-12,291.357 1999-12,283.743
# """
# 2000-12,271.892 2001-12,275.992 2002-12,333.300 2003-12,407.674 2004-12,442.974
# 2005-12,509.423 2006-12,629.513 2007-12,803.618 2008-12,819.940 2009-12,1135.012
# 2010-12,1393.512 2011-12,1652.725 2012-12,1687.342 2013-12,1221.588 2014-12,1200.440
# 2015-12,1068.317 2016-12,1152.165 2017-12,1265.674 2018-12,1249.887
# """  # noqa E501


def years_gold_value_decreased(gold_prices: str = gold_prices) -> (int, int):
    """Analyze gold_prices returning a tuple of the year the gold price
       decreased the most and the year the gold price increased the most.
    """
    years, prices = [], []
    biggest_increase, biggest_decrease = 0, 0
    year_of_largest_increase, year_of_largest_decrease = None, None

    for row in gold_prices.splitlines():
        row = row.split()
        for item in row:
            year, price = int(item.split('-12,')[0]), float(item.split('-12,')[1])
            years.append(year)
            prices.append(price)
    
    for i in range(len(prices)-1):
        if prices[i] >= prices[i+1] and\
            prices[i] - prices[i+1] > biggest_decrease:
            biggest_decrease = prices[i] - prices[i+1]
            year_of_largest_decrease = years[i+1]
        
        if prices[i] < prices[i+1] and\
            prices[i+1] - prices[i] > biggest_increase:
            biggest_increase = prices[i+1] - prices[i]
            year_of_largest_increase = years[i+1]
    
    return year_of_largest_decrease, year_of_largest_increase
        

        



print(years_gold_value_decreased())