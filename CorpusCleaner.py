"""
Created on Sun Mar 22 14:57:00 2015

@author: bigiei
"""

# Opening my csv file
dataset = open("Dataset.txt", "w")

# Opening text and isolating every word
text = open("Corpus.txt", "r")
for line in text :
    for word in line.split() :
        word = (word)
        # generating and classificating tokens     
        # finding existing tags   
        #
        # TAG CODEBOOK:
        # LSP = language for specific purpose
        #
        try:
            cleaning = word.split("/")
            token = cleaning[0]
            tag = cleaning[1]
        except IndexError:
            token = word
            # tagging non LSP as NA
            tag = "NON"
        # rimming punctuation
        if token[len(token)-1:] in char :
                token = token[:len(token)-1]
        # tagging non LSP as NA
        result = [token, tag]
        print result
        # defining result
        result = str(token + "," + tag + "\n")
        # printing token and relevant tag
        dataset.write(result)

#closing files
text.close()
dataset.close()
