#!/home/kelli/anaconda3/envs/ling/bin/python
"""Script to use regular expression to tease-out proper names and build a
list of such names that I can then use to count instances across the corpus."""

__author__ = """Kelli Wiseth (kelli@alameda-tech-lab.com)"""

# build_entity_corpus.py

import os
import re

corpus_path = '/home/kelli/dev/compling/sandbox/corpora-workups/sotu_corpus_normalized-orig/'
new_files_path = '/home/kelli/dev/compling/sandbox/named_entities/'

def main():
    os.chdir(corpus_path)
    source_files = [str(i) for i in os.listdir(corpus_path)]
 #   target_file = open(new_files_path + 'names_2-July', 'a')
    name_pattern = re.compile(r'([A-Z][a-z]+) ([A-Z][a-z]+) ([A-Z][a-z]+)')
    for file in source_files:
    #    name_pattern = re.compile(r'(\b[A-Z][a-z]+\b\s\b[A-Z][a-z]+\b){2,3}')
        # fix the below later... really inelegant, clumsy
       # name_pattern = re.compile(r'([A-Z][a-z]+) ([A-Z][a-z]+) ([A-Z][a-z]+) ([A-Z][a-z]+) ([A-Z][a-z]+) ([A-Z][a-z]+)')
        source_file = open(file, 'r')
        doc_string = source_file.read()
        for name in name_pattern.finditer(doc_string):
            print(name.group())
        source_file.close()

if __name__ == '__main__':
    main()
