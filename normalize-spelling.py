#!/home/kelli/anaconda3/envs/ling/bin/python
"""Script to conform some phrases or word spellings, eg.,
    replace 'can not' with 'cannot'.
    """

__author__ = """Kelli Wiseth (kelli@alameda-tech-lab.com)"""

# normalize_spelling.py

import os

corpus_path = '../cleancorp-pre-norm'
new_files_path = '../cleancorp-normalized/'

def main():
    os.chdir(corpus_path)
    source_files = [str(i) for i in os.listdir(corpus_path)]
    print(source_files)
    for file in source_files:
        source_file = open(file, 'r')
        doc_content = source_file.read()
        doc_content = doc_content.replace('can not', 'cannot')
        if isinstance(doc_content, string):
            print('doc_content is a string')
        target_file = open(new_files_path + file, 'w')
        target_file.write(doc_content)
        target_file.close()
        source_file.close()
if __name__ == '__main__':
    main()
