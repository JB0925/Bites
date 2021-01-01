from typing import Union
import pathlib
import csv
from io import StringIO

# Extracted from https://en.wikipedia.org/wiki/List_of_file_signatures
MAGIC_IMAGE_TABLE = """
"magic_bytes","text_representation","offset","extension","description"
"47 49 46 38 37 61
47 49 46 38 39 61","GIF87a
GIF89a",0,"gif","Image file encoded in the Graphics Interchange Format (GIF)"
"FF D8 FF DB
FF D8 FF E0 00 10 4A 46 49 46 00 01
FF D8 FF EE
FF D8 FF E1 ?? ?? 45 78 69 66 00 00","ÿØÿÛ
ÿØÿà..JFIF..
ÿØÿîÿØÿá..Exif..",0,"jpg
jpeg","JPEG raw or in the JFIF or Exif file format"
"89 50 4E 47 0D 0A 1A 0A",".PNG....",0,"png","Image encoded in the Portable Network Graphics format"
"49 49 2A 00 (little-endian format)
4D 4D 00 2A (big-endian format)","II*.MM.*",0,"tif
tiff","Tagged Image File Format (TIFF)"
"50 31 0A","P1.",0,"pbm","Portable bitmap"
"""  # noqa: E501


class FileNotRecognizedException(Exception):
    """
    File cannot be identified using a magic table
    """


def determine_filetype_by_magic_bytes(
    file_name: Union[str, pathlib.Path],
    lookup_table_string: str = MAGIC_IMAGE_TABLE,
) -> str:
    """
    file_name: file name with path
    lookup_table_string: a comma separated text containing a magic table

    Returns: file format based on the magic bytes
    """
    byte_dict = {}
    messages = {}
    file_types = 'GIF JPEG PNG TIFF PBM'.split()
    info = []
    filename = StringIO(MAGIC_IMAGE_TABLE)
    reader = csv.reader(filename)
    for row in reader:
        if row != [] and row != '\n':
            info.append(row)
    
    del info[0]
    
    for i in range(len(info)):
        byte_dict[file_types[i]] = info[i][0].lower().replace('(little-endian format)', '')\
            .replace('(big-endian format)','').replace(' ','').split('\n')
        messages[file_types[i]] = info[i][-1]
    
    byte_dict['pybites'] = ["0170796269746573000122??????666f726d6174","0170796269746573010022??????666f726d6174"]
    messages['pybites'] = "Fantasy pybites file format"
    
    with open(file_name, 'rb') as f:
        data = f.read()
        for k, v in byte_dict.items():
            for item in v:
                if b'pyb1tes' in data or b'f0rm4t' in data:
                    raise FileNotRecognizedException ('corrupted file')
                if data.hex()[:6] == item[:6] or data.hex()[2:6] == item[:4]:
                    return messages[k]
            
        raise FileNotRecognizedException ('sorry, we do not recognize this file')
        


# Set up for your convenience when coding:
#  - creates a test_image.gif GIF file
#  - calls determine_filetype_by_magic_bytes
#  - prints out file type
if __name__ == "__main__":
    test_filename = "test_image.gif"
    print(f"Script invoked directly. Writing out test file {test_filename}")
    with open(test_filename, "wb") as f:
        f.write(
            b"II*\x00\x0c\x00\x00\x00\xff\xff\xff\x00\x10\x00\x00\x01\x03"
                b"\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x01\x03\x00\x01"
                b"\x00\x00x00\x01\x00\x00\x00\x02\x01\x03\x00\x03\x00\x00\x00"
                b"\xe2\x00\x00\x00\x03\x01\x03\x00\x01\x00\x00\x00\x01\x00"
                b"\x00\x00\x06\x01\x03\x00\x01\x00\x00\x00\x02\x00\x00\x00"
                b"\x11\x01\x04\x00\x01\x00\x00\x00\x08\x00\x00\x00\x12\x01"
                b"\x03\x00\x01\x00\x00\x00\x01\x00\x00\x00\x15\x01\x03\x00"
                b"\x01\x00\x00\x00\x03\x00\x00\x00\x16\x01\x03\x00\x01\x00"
                b"\x00\x00\x80\x00\x00\x00\x17\x01\x04\x00\x01\x00\x00\x00"
                b"\x03\x00\x00\x00\x1a\x01\x05\x00\x01\x00\x00\x00\xd2\x00"
                b"\x00\x00\x1b\x01\x05\x00\x01\x00\x00\x00\xda\x00\x00\x00"
                b"\x1c\x01\x03\x00\x01\x00\x00\x00\x01\x00\x00\x00\x1d\x01"
                b"\x02\x00\x0b\x00\x00\x00\xee\x00\x00\x00(\x01\x03\x00\x01"
                b"\x00\x00\x00\x02\x00\x00\x00S\x01\x03\x00\x03\x00\x00\x00"
                b"\xe8\x00\x00\x00\x00\x00\x00\x00,\x01\x00\x00\x01\x00\x00"
                b"\x00,\x01\x00\x00\x01\x00\x00\x00\x08\x00\x08\x00\x08\x00"
                b"\x01\x00\x01\x00\x01\x00Background\x00"
        )
    print("Testing file format")
    print(determine_filetype_by_magic_bytes(test_filename))