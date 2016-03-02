#!/usr/bin/env python

# Author: Gaetano Carlucci

class Trie:

	def __init__(self):
		self.root = {"number": 0} # number of words in the trie

	def getRoot(self):
		return self.root 

	# @param {string} word
	# @return {void}
	# Inserts a word into the trie.
	def insert(self, word):
		if self.find(word):
		   return False

		node = self.root
		# '#' defines the end of the word
		word = word + '#'
		print word
		for char in word:
			#  do not insert the char if it is already in the trie
			if char not in node:
				node[char] = {}
			node = node[char]
		self.root["number"] += 1
	
	def find(self, word):
		node = self.root
		# '#' defines the end of the word
		word = word + '#'
		for char in word:
			if char not in node:
				return False
			else:
				node = node[char]
		return True
		
	def remove(self, word):
		# check if the word exists
		if not self.find(word):
		   return False

		if self.root["number"] == 1: 
		   self.root = {"number": 0}
		   return True
		
		# '#' defines the end of the word
		word = word + '#'
		while len(word) > 0 :
			node = self.root
			#goes to the end of the word in the trie
			for char in word:
				node = node[char]	
			
			if len(node.keys()) > 1:
				del node[keyToRemove]
				return True
			#this is the char that we will possibly remove form the trie in the next iteration
			keyToRemove = word[-1]
			word = word[:-1]
		self.root["number"] -= 1



if __name__ == '__main__':
	test = Trie()
	test.insert('ciao')
	test.insert('cubo')
	test.insert('dado')
	print test.getRoot()
	print test.find('caso')
	print test.find('ciao')
	test.remove('ciao')
	print test.getRoot()
