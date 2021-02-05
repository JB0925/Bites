from decimal import Decimal 

def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    if item_total == '$0.00':
        return item_total, [Decimal('0.00').quantize(Decimal('0.00'))]
    
    tax_rate = float(tax_rate[:-1])
    item_total = float(item_total[1:])
    tip = float(tip[:-1]) / 100
    tax = tax_rate / 100
    tax_added = item_total * tax 
    total_before_tip = round(item_total + tax_added, 2)
    tip_amount = total_before_tip * tip
    if len(str(tip_amount)) > 3:
        if str(tip_amount).split('.')[1][2] == '5':
            tip_amount += 0.005
    total_after_tip = round(total_before_tip + tip_amount, 2)
    grand_total = total_after_tip
    splits = []
    
    if len(str(grand_total).split('.')[1]) == 1:
        grand_total = str(grand_total) + '0'
    
    while people:
        even_distribution = round(total_after_tip / people, 2)
        total_after_tip -= even_distribution
        even_distribution = Decimal(str(even_distribution)).quantize(Decimal('0.00'))
        splits.append(even_distribution)
        people -= 1 
        
    return f'${grand_total}', splits
    

info = ('$0.00', '0%', '0%', 1)
print(check_split(*info))

