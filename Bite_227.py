from os import read
from pathlib import Path
import csv
import json
from json.decoder import JSONDecodeError
import requests

EXCEPTION = 'exception caught'
TMP = Path('/tmp')

url = 'https://bites-data.s3.us-east-2.amazonaws.com/mount-data1.json'
request = requests.get(url).text


def convert_to_csv(json_file):
    """Read/load the json_file (local file downloaded to /tmp) and
       convert/write it to defined csv_file.
        The data is in mounts > collected

       Catch bad JSON (JSONDecodeError) file content, in that case print the defined
       EXCEPTION string ('exception caught') to stdout reraising the exception.
       This is to make sure you actually caught this exception.

       Example csv output:
       creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
       32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
       63502,ability_mount_hordescorpionamber,True,...
       ...
    """  # noqa E501
    #csv_file = TMP / json_file.name.replace('.json', '.csv')
    csv_file = 'testbite227.csv'

    try:
        reader = json.loads(json_file)['mounts']['collected']

    except JSONDecodeError:
        print(EXCEPTION)
        raise
    
    else:
        count = 0
        
        with open(csv_file, 'w') as f:
            for item in reader:
                data = csv.DictWriter(f, item.keys())
                if count == 0:
                    data.writeheader()
                    count += 1
                data.writerow(item)




print(convert_to_csv(request))
    