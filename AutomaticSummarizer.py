# -*- coding: utf-8 -*-

# Import
from __future__ import division
import nltk, re
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
		tokenizer = RegexpTokenizer('\W+')
		words = [word.lower() for word in tokenizer.tokenize(input)]
		words = [word for word in words if word not in stopwords.words()]
		freqWords = FreqDist(words)
		
		most_freq = [pair[0] for pair in freqWords.items()[:100]]
		
		print most_freq
		return "abc"
		
# Main method - run by going to folder C:/Python27 and then python <location of python file>
def main():
	
	# Object of class AutomaticSummarizeTool
	summObj = AutomaticSummarizerTool()
	
	# Fetching Data from the text file containing the news
	dataFile = open('E:/PythonProjects/news.txt', 'r')
	lines = dataFile.read()
	para = summObj.split_to_paragraphs(lines)
	title = para[0]
	
	# Print resulst 	
	print "Title: \n" + title
	print ""
	print "Summary extracted from first few lines: \n" + para[1]

	inputList = dataFile.readlines()
	abc = summObj.get_summary(lines)

if __name__ == '__main__':
	main()		
	
