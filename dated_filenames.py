#!/home/kelli/dev/git-repo/compling/dated_filenames.py
"""Script to rename the corpus files so that they include the year of SOU. """

__author__ = """Kelli Wiseth (kelli@alameda-tech-lab.com)"""

# dated_filenames.py

import os
import re

corpus_path = '../fix_filenames/'
new_files_path = '../fixed_filenames/'

def main():
    os.chdir(corpus_path)
    source_files = [str(i) for i in os.listdir(corpus_path)]
    print(source_files)
    for file in source_files:
        source_file = open(file, 'r')
        doc_content = source_file.read()
        source_file = open(file, 'r')
        line = source_file.readline()
        year = re.findall(r'\d{4}', line)
#        print(year[0])
#       if isinstance(year, list):
#           print('year is a list')
        new_file = year[0] + '-' + file
        target_file = open(new_files_path + new_file, 'w')
        target_file.write(doc_content)
        target_file.close()
        source_file.close()
if __name__ == '__main__':
    main()
