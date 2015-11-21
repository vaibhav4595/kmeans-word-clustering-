How to run


the following the command

python main.py filename option option2

filename - contains the datafile name

option2 - a filename or 0
     include 0 in every case except when option = 3
     in that case whrn option = 3, provide the filename of the stop word file

option - any one of 1 or 2 or 3 or 4
      when option = 1 : returns the cooccurrence matrix
      when option = 2 : returns the cluster of words without excluding stop words
      when option = 3 : returns the cluster of words excluding stop words
      when option = 4 : returns the cluster of words excluding top 50 words



example :
     you want to find clusters without stop words the
                    '  python main.py dataset.txt 2 0 '
     you want to find the clusters with stop words then
                    '  python main.py dataset.txt 3 stopword.txt '
