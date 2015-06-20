# This is the first draft of a MRJob word counter.
#
# To do: syntax sensitive N-Gram finder
#
#import itertools

from mrjob.job import MRJob
import string


class MRTextCount(MRJob):
	def mapper(self, _, text):


		sentences = []
		words = []

		# Non exaustive punctuation set
		char = [".", "!", "?"]

		# Text wrangling
		for phrase in text.split(". "):
			# Remove sentence end punctuation
			if phrase[-1:] in char:
				phrase = phrase.strip(phrase[-1:])
				# Appending words
			words.append(phrase.split(" "))
	
		# Issue: in-sentence punctuation is still there
		print words

		yield 'sentences', len(words)

		# Unpacking lists
		for i in words:

			sentence = i
			for i in sentence:
				yield i, 1

def reducer(self, i, counts):
		yield i, sum(counts)


if __name__ == '__main__':
	MRTextCount.run()
