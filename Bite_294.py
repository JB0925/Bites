test = '8/9-X X 6/4/X 8-X XXX'
test2 = '169-X X 8-41X X 9-53'
test3 = '-7188/9-X X X X X XXX'
test4 = '8/549-X X 5/53639/9/X'
test5 = '36546/819/7--/717/3/-'
test6 = 'X 9/8/7/6/5/4/3/2/X1/'
test7 = 'X -/X 5-8/9-X 811-4/X'
test8 = '6271X 9-8/X X 35725/8'
test9 = 'X 7/729/X X X 236/7/3'


def calculate_score(frames: str) -> int:
    """Calculates a total 10-pin bowling score from a string of frame data."""
    spare = '/'
    strike = 'X'
    gutter_ball = '0'
    digits = '0123456789'
    numstack = []
    frames = frames.replace(' ', '').replace('-', gutter_ball)
    copy_frames = []

    for item in list(frames):
        if item == strike:
            item += '+'
            copy_frames.append(item)
        copy_frames.append(item)
    
    copy_frames = ''.join(copy_frames)
    
    for i in range(len(copy_frames)-2):
        if copy_frames[i] in digits and copy_frames[i+1] in digits:
            if copy_frames[i-1] == strike:
                numstack.append(copy_frames[i:i+2])
            if i % 2 == 0:
                numstack.append(copy_frames[i:i+2])
    
    for i in range(len(frames)-2):
        if frames[i] == spare:
            numstack.append(frames[i-1:i+2])
        if frames[i] == strike:
            numstack.append(frames[i:i+3])
    
    if frames[-2:] not in numstack[-1]:
        if frames[-2] == spare:
            numstack.append(frames[-3:])
        else:
            numstack.append(frames[-2:])
    
    if frames[-2] in digits and frames[-1] in digits and len(numstack[-1]) == 3:
        if frames[-2:] not in numstack and len(numstack) < 10:
            numstack.append(frames[-2:])
    
    return numstack


def get_total(numstack):
    total = 0
    spare = '/'
    strike = 'X'
    gutter_ball = '0'
    digits = '0123456789'

    for item in numstack:
        if spare in item and strike not in item:
            d = 10 - int(item[0])
            temp = [int(n) for n in item if n in digits]
            temp.append(d)
            total += sum(temp)
        
        if strike in item and spare not in item:
            temp = [int(n) for n in item if n in digits]
            total += ((item.count(strike) * 10) + (sum(temp)))
        
        if strike in item and spare in item:
            total += 20
        
        if all(d in digits for d in item):
            temp = [int(n) for n in item]
            total += sum(temp)
    
    return total



numstack = calculate_score('X X X X X X X X X XXX')
print(get_total(numstack))

    