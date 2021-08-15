#!/home/kelli/anaconda3/envs/ling/bin/python
"""Script to process state of union texts that contain multiple
 state of union addresses. The files contain varying numbers of
 SOU addresses demarcated by *** between the text. The files
 are held in the /dev/compling/sandbox/corpus_to_extract. """

__author__ = """Kelli Wiseth (kelli@alameda-tech-lab.com)"""

# extractor.py

import os

corpus_path = '../corpus_to_extract/'
new_files_path = '../extracted_files/'

def main():
    os.chdir(corpus_path)
    source_files = [str(i) for i in os.listdir(corpus_path)]
    print(source_files)
    for file in source_files:
        source_file = open(file, 'r')
        doc_string = source_file.read()
        new_strings = doc_string.split('***')
        for i in range(0, len(new_strings)):
            new_file = file + str(i)
            target_file = open(new_files_path + new_file, 'w')
            target_file.write(new_strings[i])
            target_file.close()
        source_file.close()
if __name__ == '__main__':
    main()
