# tOYO

## Business Background

The ebook reader "OYO" (see https://de.wikipedia.org/wiki/OYO) cannot display Cyrillic cursive fonts
properly. 

These are displayed as follows: ???????????? ?? ???? ?????? ???? 

tOYO should fix this issue for the EPUB file format by removing all cursive formatting (italics).  


## Specification 

### EPUB

An ePub publication is delivered as a single file. 
This file is an unencrypted zipped archive containing a set of interrelated resources.
The publication's content is stored as XHTML. 


### Solution Sketch

INPUT: EPUB file (E) 

1. Unzip E
2. Iterate through the content files and replace all cursive fonts. Examples: \<em></em>, \<blockquote></blockquote>
2.1. The set of the replaced elements should be configurable. 
3. Zip E

OUTPUT: EPUB file without cursive fonts (E')