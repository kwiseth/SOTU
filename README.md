# compling
These Python scripts handle the preliminary file clean up for my State of 
the Union (SOTU) project. [TODO: Add details about the goals of this project]


From [Internet Archive](http://archive.org), I downloaded all available SOTU text files to use my corpus. Some of the files contained text of all speeches for a given President, while others were individual files already. The `extractor.py` script extracts each speech into its own file. After that, the `dated_filenames.py` opens each of these single files and extracts the date of the SOTU, then creates a new file with the year as part of the filename. 

With this semi-cleaned up corpus, I ran `significant_words.py` again, using different SOTUs as my target, but that test run revealed that I still need to handle named entities. In short, there's still a lot of work to do. The files in this repository at this point are basically all about cleaning up data to provide a 

#### TODO

1. Normalize spelling as much as possible ("can not" vs "cannot" vs "can't"?) 
2. Write decent commments for each python script
3. Use regex to handle named entities in all their forms ("fname lname", "lname", "fname" (after first reference)

