# DigitalHumanitiesMiniProject

Project Link: https://sagivnet.wixsite.com/hebrewlovesongs

Purposes:
- Applying LemLDA algorithm for topic modeling on a lyrics corpus represented by XML files containing the fields of lyrics, singer, writer   and composer.
- 
- Analyzing the data given by the LemLDA algorithm.
- Creating statistics about a specific category:
    1. Top 10 

How to use:
  1. MakeTxt.py - Takes the folder containing xml files and exctracts the lyrics to txt files keeping the same folder partition.
  2.1 UseHebTok.py [Optional] - Applying 2.2 on each txt file while keeping the same folder partition.
  2.2 hebtokenizer.py [Optional] - Fix a certain problem with hebrew text files to match LemLDA algorithm input.
  3. MakeHtmlHeb.py - Gets a link of a specific topic and generates a txt file with each line containing the singer and song.
  4. ExctractData.py - Gets a data txt file (from step 3) and extracts the data of writer and composer from the matched XML file.
  5.* MakeSet<>.py - Takes all extracted data files (from step 4) aggregating the data removing duplicates from different data files.
  6. makeTop10.py - Takes all 3 generated data from step 5.1, 5.2 and 5.3 and makes 3 folders (Singers, Writers, Composers). Each folder     will have 10 files in it, each file named as following: Rank. Name (e.g 1. חוה אלברשטיין). Each file contains all specific topic     related songs of the artist sorted by the alphabetic order.
