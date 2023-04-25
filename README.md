# SOTU
### State of the Union speeches, linguistic analyses

These Python scripts handle the preliminary file clean up for my State of 
the Union (SOTU) project. This project aims to be a diachronic analysis of the speech or writing styles of U.S. presidents. Prior to XXXX, state of the union updates were letters written to Congress. Given that, I might break up this project into two distinct phases: written letters from US presidents to Congress and speeches delivered to Congress. I've had to put this project aside for the past several years, and am only now (2023) returning to it, along with doing the historical research. 

Process thus far: From [Internet Archive](http://archive.org), I downloaded all available SOTU text files to use as my corpus. Some of the files contained text of all speeches for a given President, while others were already individual files. The `extractor.py` script extracts each speech into its own file. After that, the `dated_filenames.py` opens each of these single files and extracts the date of the SOTU speech from the text file, then creates a new file with the year as part of the filename. (I obtained some of the data files from the [NLTK corpora (state_union)](http://www.nltk.org/nltk_data/)).

There's still a lot of clean up and data prep work to do.

#### TODO

1. Normalize spelling as much as possible ("can not" vs "cannot" vs "can't"). The `normalize_spelling.py` script is just a start. 
2. Figure out how to handle named entities, without losing references to important historical figures (eg, cabinet members, military leaders, etc). Perhaps 'citizen' for others? 
3. Write decent commments for each python script
4. Use regex to handle named entities in all their forms ("fname lname", "lname", "fname" (after first reference)

