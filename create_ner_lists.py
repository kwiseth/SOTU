#!/home/kelli/anaconda3/envs/ling/bin/python
"""Script to extract people, places, other Named entities from the SOTU corpus.
 This is part of the preliminary corpus cleanup work for the SOTU project."""

__author__ = """Kelli Wiseth (kelli@alameda-tech-lab.com)"""

# create_ner_lists.py

import os
# import re

corpus_path = '../named_entity_references/'
source_file = 'ner_data_raw_sorted.txt'
people_file = 'people_ner.txt'
# gpe_file = 'gpe_ner.txt'
# places_file = 'places_ner.txt'
people_ner = {}
people = []

def main():
    os.chdir(corpus_path)
    source_data = open(corpus_path + source_file, 'r')
    text_lines = source_data.readlines()
    for line in text_lines:
        words = line.split()
        word_ctr = len(words)
        ner_type = word_ctr - 1
        for i in range(0, len(words)):
            if words[ner_type] == 'PERSON':
                person = line.removesuffix(': PERSON\n')
#                print(person)
                people.append(person)
                if person in people_ner:
                    people_ner[person] = people_ner[person]+1
                else:
                    people_ner[person] = 1

    people_list = people_ner.keys()
    print(people_list)
    output = open(people_file, 'w')
    output.write(str(people_list))
    source_data.close()
    output.close()

if __name__ == '__main__':
    main()