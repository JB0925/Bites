DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1

small_grid = """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""

intermediate_grid = """
43 - 44 - 45 - 46 - 47 - 48 - 49
 |
42   21 - 22 - 23 - 24 - 25 - 26
 |    |                        |
41   20    7 -  8 -  9 - 10   27
 |    |    |              |    |
40   19    6    1 -  2   11   28
 |    |    |         |    |    |
39   18    5 -  4 -  3   12   29
 |    |                   |    |
38   17 - 16 - 15 - 14 - 13   30
 |                             |
37 - 36 - 35 - 34 - 33 - 32 - 31
"""

big_grid = """
73 - 74 - 75 - 76 - 77 - 78 - 79 - 80 - 81
 |
72   43 - 44 - 45 - 46 - 47 - 48 - 49 - 50
 |    |                                  |
71   42   21 - 22 - 23 - 24 - 25 - 26   51
 |    |    |                        |    |
70   41   20    7 -  8 -  9 - 10   27   52
 |    |    |    |              |    |    |
69   40   19    6    1 -  2   11   28   53
 |    |    |    |         |    |    |    |
68   39   18    5 -  4 -  3   12   29   54
 |    |    |                   |    |    |
67   38   17 - 16 - 15 - 14 - 13   30   55
 |    |                             |    |
66   37 - 36 - 35 - 34 - 33 - 32 - 31   56
 |                                       |
65 - 64 - 63 - 62 - 61 - 60 - 59 - 58 - 57
"""

def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    direction = 'right'
    two_dimensional_grid = []

    grid = grid.replace('-', '').replace('|', '').replace('  ',' ').splitlines()
    two_dimensional_grid.append([item.replace('  ', ' ') for item in grid if item != '' and item[0].isnumeric()])
    
    for i in range(len(two_dimensional_grid[0])):
        item = two_dimensional_grid[0][i].split()
        two_dimensional_grid.append([int(x) for x in item])
    
    tdg = two_dimensional_grid[1:]
    ordered_nums = [1]
    k = 0
    
    for i in range(len(tdg)):
        for j in range(len(tdg[0])):
            if tdg[i][j] == START_VALUE:
                start_coordinates = [i,j]
                sr, sc = start_coordinates[0], start_coordinates[1]
                while tdg[sr][sc] != max(max(x) for x in tdg):
                    try:
                        if sc+1 != len(tdg) and tdg[sr][sc+1] == ordered_nums[-1] + 1:
                            if direction != 'right':
                                direction = 'right'
                                print(' '.join(str(x) for x in ordered_nums)+ ' ' + RIGHT)
                                ordered_nums.clear()
                            ordered_nums.append(tdg[sr][sc+1])
                            if sc != len(tdg[0]) - 1:
                                sc += 1
                        if tdg[sr][sc-1] == ordered_nums[-1] + 1:
                            if direction != 'left':
                                direction = 'left'
                                print(' '.join(str(x) for x in ordered_nums)+ ' ' + LEFT)
                                ordered_nums.clear()
                            ordered_nums.append(tdg[sr][sc-1])
                            if sc != 0:
                                sc -= 1
                        if tdg[sr-1][sc] == ordered_nums[-1] + 1:
                            if direction != 'up':
                                direction = 'up'
                                print(' '.join(str(x) for x in ordered_nums)+ ' ' + UP)
                                ordered_nums.clear()
                            ordered_nums.append(tdg[sr-1][sc])
                            if sr != 0:
                                sr -= 1
                        if tdg[sr+1][sc] == ordered_nums[-1] + 1:
                            if direction != 'down':
                                direction = 'down'
                                print(' '.join(str(x) for x in ordered_nums)+ ' ' + DOWN)
                                ordered_nums.clear()
                            ordered_nums.append(tdg[sr+1][sc])
                            if sr != len(tdg) - 1:
                                sr += 1

                    except IndexError:
                        pass
                    
    print(' '.join(str(x) for x in ordered_nums))

                    
print(print_sequence_route(big_grid))