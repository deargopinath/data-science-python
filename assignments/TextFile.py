f= open("assignment.txt","w+")
f.write("I want to go home after lunch.")
f.write(" It would be better\n")
f.close()

from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg
sample = gutenberg.raw("shakespeare.txt")
token = sent_tokenize(sample)
for para in range(2):
    print(token[para])