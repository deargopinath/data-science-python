# Case Study 
# Consider the text that you have imported from the file 'shakespeare.txt'. Obtain the 
# list of meaningful words as separate items of the list. Also determine the list of most 
# frequent bigrams. 

import nltk
nltk.download
from nltk.collocations import BigramCollocationFinder
bigram_measures = nltk.collocations.BigramAssocMeasures()
text = "Shall I compare thee hath hath to a summer's day? Thou art hath hath more lovely and more more temperate Rough winds do hath hath shake shake the darling buds of May,"
finder = BigramCollocationFinder.from_words(nltk.word_tokenize(text))
finder.nbest(bigram_measures.pmi, 5)
