#!/home/kelli/anaconda3/envs/ling/bin/python
"""Script to generate named entities in source text files and
 output to another text file."""

__author__ = """Kelli Wiseth (kelli@alameda-tech-lab.com)"""

# build_ner_corpus.py

import os
import spacy

corpus_path = '/home/kelli/dev/compling/sandbox/corpora-workups/sotu_corpus_normalized/'
new_files_path = '/home/kelli/dev/compling/sandbox/named_entities/'

def main():
    os.chdir(corpus_path)
    source_files = [str(i) for i in os.listdir(corpus_path)]
    target_file = open(new_files_path + 'ner_ju', 'a')
    for file in source_files:
        nlp = spacy.load('en')
        source_file = open(file, 'r')
        doc_string = source_file.read()
        document = nlp(doc_string)

#        print("Noun phrases:", [chunk.text for chunk in document.noun_chunks])
#        print("Verbs:", [token.lemma_ for token in document if token.pos_ == "VERB"])
        for entity in document.ents:
            print(f'{entity.text}: {entity.label_}', file=target_file)
        source_file.close()

if __name__ == '__main__':
    main()
