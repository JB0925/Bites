import csv


full = """
17409,"Matheson, Rick",,,,,,,,,,
36283,"Jones, Tom",SCI09-4 - SU,MATH09-2 - PH,TA09-1 - AB,IS09-4 - LM,SCI09-3 - NdN,MATH09-2 - RB,DE09-3 - KmQ,ENG09-3 - KaR,PE09-3 - PS
99415,"Blake, Arnold",,,,,,,,,,
"""

partial = """
17409,"Jones, Tom",,,,,,,,,,
17409,"Matheson, Rick",,IS09-1 - BR,,SCI09-4 - SU,MATH09-2 - RB,,ENG09-4 - LE,,PE09-1 - MR,
99415,"Blake, Arnold",,,,,,,,,,
"""

empty = """
99415,"Blake, Arnold",,,,,,,,,,
21692,"Prest, Phil",,,,,,,,,,
36283,"Jones, Tom",,,,,,,,,,
"""

def class_rosters(input_file):
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
    roster_data = []

    for row in input_file.splitlines():
        row = row.split(',')
        row = [item for item in row if item != '']
        try:
            student_id = row[0]
            year = '2020'
            classes = [item.split(' - ')[0] for item in row[3:]]
            for class_ in classes:
                data = f'{class_},{year},{student_id}'
                roster_data.append(data)
        except Exception:
            pass
    
    return roster_data




print(class_rosters(full))