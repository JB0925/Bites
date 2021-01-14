STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""
    width = (rows * 2) - 1
    num_spaces = 1
    tree = []

    for i in range(1,rows+1):
        # if i == 1:
        #     #print(' ' * (width) + STAR)
        #     tree.append(' ' * (width) + STAR)

        # for j in range(0, width):
        #     #print(end=' ')
        #     pass
        
        width -= 1

        if i == 1:
            star = ' ' * (i*2-2) +STAR
            tree.append((star).center(rows*2))
        l = LEAF * (i*2-1)
        tree.append(l.center(rows*2))
        
    for _ in range(2):
        while True:
            poles = ((rows * 2 - 1) - num_spaces)
            if num_spaces == ((rows*2-1) // 2): 
                break
            else:
                num_spaces += 1

        if poles % 2 == 0:
            poles += 1
            num_spaces -= 1
        
        trunks = f"{' ' * (num_spaces//2)}{TRUNK*poles}{' ' * (num_spaces//2)}"
        tree.append((trunks).center(2*rows))
    
    return '\n'.join([line for line in tree])
    
    
    
    


print(generate_improved_xmas_tree())