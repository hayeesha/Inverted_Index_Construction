Inverted_Index_Construction
===========================

 This is a python script that constucts an inverted index for terms in a corpus of 2,916 emails. The contents in these emails
 are represented as a bag of words.
 
 Method
 =======
  The script uses a dictionary to store the terms in the corpus and the number of documents each term appears in. The result
  is stored in a file called dictionary.txt
  
  The postings list for each term which shows the name of the document and the number of times a term appears in the document\
  is stored in a file PostingsList.txt
  
  Uses
  =====
    The main purpose of this program is for query processing. That is queries involving terms in the corpus.
