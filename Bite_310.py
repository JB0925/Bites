import re
from copy import copy

files = ["NCTC8325_S1_L001_R1_001.fastq.gz","NCTC8325_S1_L001_R2_001.fastq.gz",
         "E.coliK12_S2_L001_R1_001.fastq.gz","E.coliK12_S2_L001_R2_001.fastq.gz",
         "C.elegans_S3_L001_R1_001.fastq.gz","C.elegans_S3_L001_R2_001.fastq.gz"]

files2 = [
                "C.elegans_S3_L001_R2_001.fastq.gz",
                "E.coliK12_S2_L001_R2_001.fastq.gz",
                "NCTC8325_S1_L001_R2_001.fastq.gz",
                "E.coliK12_S2_L001_R1_001.fastq.gz",
                "NCTC8325_S1_L001_R1_001.fastq.gz",
                "C.elegans_S3_L001_R1_001.fastq.gz"
            ]

files3 = [
                "NCTC8325_S1_L001_R1_001.fastq.gz",
                "NCTC8325_S1_L001_R2_001.fastq.gz",
                "E.coli_S2_L001_R1_001.fastq.gz",
                "E.coliK12_S2_L001_R2_001.fastq.gz",
                "C.elegans_S3_L001_R1_001.fastq.gz",
                "C.elegans_S4_L001_R2_001.fastq.gz"
            ]

files4 = [
                "NCTC8325_S1_L002_R1_001.fastq.gz",
                "NCTC8325_S1_L002_R2_001.fastq.gz",
                "C.elegans_S3_L003_R1_001.fastq.gz",
                "C.elegans_S4_L003_R2_001.fastq.gz"
            ]

files5 = [
                "NCTC_8325_S1_L001_R1_001.fastq.gz",
                "NCTC_8325_S1_L001_R2_001.fastq.gz",
                "C._ele_gans_1_S3_L001_R1_001.fastq.gz",
                "C._ele_gans_1_S3_L001_R2_001.fastq.gz"
            ]

files6 = [
                "NCTC8325_S1_L001_R1_001.fastq.gz",
                "NCTC8325_S1_L001_R2_001.fastq.gz",
                "E.coliK12_S2_L001_R3_001.fastq.gz",
                "E.coliK12_S2_L001_R4_001.fastq.gz",
                "C.elegans_S3_L001_R1_001.fastq.gz",
                "C.elegans_S3_L001_R3_001.fastq.gz"
            ]

files7 = [
                "folder/NCTC8325_S1_L001_R1_001.fastq.gz",
                "folder/NCTC8325_S1_L001_R2_001.fastq.gz",
                "folder/E.coliK12_S2_L001_R1_001.fastq.gz",
                "folder/E.coliK12_S2_L001_R2_001.fastq.gz",
                "folder/C.elegans_S3_L001_R1_001.fastq.gz",
                "folder/C.elegans_S3_L001_R2_001.fastq.gz"
            ]

files8 = [
                "folder/NCTC8325_S1_L001_R1_001.FASTQ.GZ",
                "folder/NCTC8325_S1_L001_R2_001.FASTQ.GZ",
                "folder/E.coliK12_S2_L001_R1_001.FASTQ.GZ",
                "folder/E.coliK12_S2_L001_R2_001.FASTQ.GZ",
                "folder/C.elegans_S3_L001_R1_001.FASTQ.GZ",
                "folder/C.elegans_S3_L001_R2_001.FASTQ.GZ"
            ]

files9 = [
                "folder/NCTC8325_S1_L001_R1_001.FASTQ.GZ",
                "folder/NCTC8325_S1_L001_R2_001.FASTQ.GZ",
                "folder/E.coliK12_S2_L001_R1_001.fastq.gz",
                "folder/E.coliK12_S2_L001_R2_001.FASTQ.GZ",
                "folder/C.elegans_S3_L001_R1_001.fastq.GZ",
                "folder/C.elegans_S3_L001_R2_001.FASTQ.gz"
            ]

files10 = [
                "NCTC8325_S1_L001_r1_001.fastq.gz",
                "NCTC8325_S1_L001_r2_001.fastq.gz",
                "E.coliK12_S2_l001_R1_001.fastq.gz",
                "E.coliK12_S2_l001_r2_001.fastq.gz",
                "C.elegans_s3_L001_r1_001.fastq.gz",
                "C.elegans_s3_L001_R2_001.fastq.gz"
            ]

files11 = [
                    "NCTC8325_S1_L001_R1_001.fastq.gz.fastq.gz",
                    "NCTC8325_S1_L001_R2_001.fastq.gz.fastq.gz"
                ]

files12 = [
                "NCTC8325_S_L001_R1_001.fastq.gz",
                "NCTC8325_S_L001_R2_001.fastq.gz"
            ]

files13 = [
                "NCTC8325_S1_L001_R1_001.fastq.gz",
                "NCTC8325_S1_L001_R1_001.md5.gz",
                "NCTC8325_S1_L001_R2_001.md5.gz",
                "NCTC8325_S1_L001_R2_001.fastq.gz",
                "C.elegans_S3_L001_R1_001.md5.gz",
                "C.elegans_S3_L001_R2_001.md5.gz"
            ]




def pair_files(filenames):
    """
    Function that pairs filenames

    filenames: list[str] containing filenames
    returns: list[tuple[str, str]] containing filename pairs
    """
    filenames = re.findall(r'[A-Za-z0-9\.:/_]+_S?s?[1-9]+_L?l?[0-9]{3}_R?r?1?2?_[0-9]{3}\.[^m][\w]+\.[\w]+(?![\w\.]+)', ' '.join(filenames))
    filelist = []
    copyfiles = []
    #filenames = [item for item in filenames if 'R1' in item or 'R2' in item or 'r1' in item or 'r2' in item]
    num = len(filenames)
    first = None
    last = None
    

    for i in range(num):
        for f in filenames[i+1:]:
            if f.lower() != filenames[i].lower():
                f1, f2 = filenames[i].split('_'), f.split('_')
                if f1[0:3] == f2[0:3]:
                    if 'R1' in f1 or 'r1' in f1:
                        first, last = filenames[i], f
                        filelist.append((first, last))
                    elif 'R1' in f2 or 'r1' in f2:
                        first, last = f, filenames[i]
                        filelist.append((first, last))
                    else:
                        continue
                    
    
    return sorted(filelist)


# Set up for your convenience during testing
if __name__ == "__main__":
    filenames = [
        "Sample1_S1_L001_R1_001.FASTQ.GZ",
        "Sample1_S1_L001_R2_001.fastq.gz",
        "Sample2_S2_L001_R1_001.fastq.gz",
        "sample2_s2_l001_r2_001.fastq.gz",
    ]
    # ('Sample1_S1_L001_R1_001.FASTQ.GZ', 'Sample1_S1_L001_R2_001.fastq.gz')
    # ('Sample2_S2_L001_R1_001.fastq.gz', 'sample2_s2_l001_r2_001.fastq.gz')

    # for pair in pair_files(files):
    #     print(pair)

    print(pair_files(files13))