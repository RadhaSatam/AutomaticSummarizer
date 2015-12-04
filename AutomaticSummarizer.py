# Imports
from __future__ import division
import nltk, re, unicodedata
from nltk import *
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# Automatic Summarizer of News Articles
# Created by Radha Satam
# December 12, 2015
# For CIS 496H (Instructor: Gabriel Murray)

class AutomaticSummarizerTool(object):

	# Function to split text into sentences
	def split_to_sentences(self, content):
		content = content.replace("\n", ". ")
		return content.split(". ")
	
	# Function to split text into paragraphs
	def split_to_paragraphs(self, content):
		return content.split("\n\n")
		
	def summarizeFromFreqDist(self, input):
		return " ".join(self.get_summary(input))
		
	def get_summary(self, input):
		tokenizer = RegexpTokenizer('\w+|\$[\d\.]+')
		
		# Get all the words in the lower case
		words = [word.lower() for word in tokenizer.tokenize(input)]

		# Remove the stop words like the, and, or, etc.
		words = [word for word in words if word not in stopwords.words()]
		
		# Frequency of each word in input
		freqWords = FreqDist(words)		
		most_freq = [word[0] for word in freqWords.most_common(20)]
		
		# actual_sents contains all the original sentences with the case intact
		actual_sents = self.split_to_sentences(input)
		actual_sents[:] = [item for item in actual_sents if item != '']
		num_sentences = len(actual_sents)
		
		# working_sents contains the senteces with lower case -- will allow for comparison
		working_sents = [sentence.lower() for sentence in actual_sents]
		
		# output_sents - emtpy list to store the sentences that contain most frequent words
		output_sents = []
		
		# num_freqWords_inSents stores the number of times a frequent word occurs in each of the sentences
		num_freqWords_inSents = [0] * num_sentences	

		# Loop through each frequent word and add to ouput sents if 
		for i in range(0, num_sentences):
			for word in most_freq:
					if (word in working_sents[i]):
						num_freqWords_inSents[i] = num_freqWords_inSents[i] + 1
						if(actual_sents[i] not in output_sents):
							output_sents.append(actual_sents[i])
					
		num_freqWords_inSents[:] = [item for item in num_freqWords_inSents if item != 0]
		zip_op_num = zip(num_freqWords_inSents, output_sents)
		
		# Rearranges the output sentences to include the sentences which contain the most frequent words first
		output_priority = [y for (x,y) in sorted(zip_op_num, reverse=True)]
		
		# Fetches first 3 senteces that contain the most number of frequent words in it		
		relevant_output = output_priority[0:3]
		
		# sort the output sentences back to their original order
		return self.reorder(relevant_output, input)
		
	# Function to sort the ouput in the order of occurrence in the article
	def reorder( self, output_sents, input ):
		output_sents.sort( lambda s1, s2: 
			input.find(s1) - input.find(s2) )
		return output_sents
		
# Main method - run by going to folder C:/Python27 and then python <location of python file>
def main():
	
	# Object of class AutomaticSummarizeTool
	summObj = AutomaticSummarizerTool()
	
	# Fetching Data from the text file containing the news
	dataFile = open('E:/PythonProjects/AutomaticSummarizer/news2.txt', 'r')
	lines = dataFile.read()
	lines = (lines.decode("utf-8")).encode("ascii","ignore")
	
	para = summObj.split_to_paragraphs(lines)
	
	title = para[0]
	
	# Print resulst 	
	print "Title: " + title
	print ""
	print "Summary extracted from first few lines: \n\n" + para[1]
	print ""
	
	abc = summObj.get_summary(lines)
	
	print "Summary based on Frequency Distribution of words: \n\n" + abc[1] + abc[2]
	
if __name__ == '__main__':
	main()		
	
