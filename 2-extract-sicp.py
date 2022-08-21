#import zipfile
import os

TEXTBOOK = 'SICP_FULLTEXT.zip'

os.system(f'unzip {TEXTBOOK}')   # dependency, unzip


#skipping below for now.
#with zipfile.ZipFile(TEXTBOOK, mode="r") as sicp_archive:
#    for file in sicp_archive.printdir():
#        print(file)

