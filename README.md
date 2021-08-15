# SOTU
### State of the Union speeches, linguistic analyses

These Python scripts handle the preliminary file clean up for my State of 
the Union (SOTU) project. [TODO: Add details about the goals of this project]

From [Internet Archive](http://archive.org), I downloaded all available SOTU text files to use as my corpus. Some of the files contained text of all speeches for a given President, while others were individual files already. IIRC, I might also have obtained some files from the [NLTK corpora (state_union)](http://www.nltk.org/nltk_data/), which covers 1945-2004. The `extractor.py` script extracts each speech into its own file. After that, the `dated_filenames.py` opens each of these single files and extracts the date of the SOTU speech from the text file, then creates a new file with the year as part of the filename. 


There's still a lot of clean up and data prep work to do.

#### TODO

1. Normalize spelling as much as possible ("can not" vs "cannot" vs "can't"). The `normalize_spelling.py` script is just a start. 
2. Figure out how to handle named entities, without losing references to important historical figures (eg, cabinet members, military leaders, etc). Perhaps 'citizen' for others? 
3. Write decent commments for each python script
4. Use regex to handle named entities in all their forms ("fname lname", "lname", "fname" (after first reference)

