import string
import traceback
#write a custom exception, then an inclusive test, then write the code for the following functions:

class PunctuationException(Exception):

	def __str__(self):
		return "String contains irreversible character!"

def shout(txt):
	if type(txt) != str:
		raise TypeError("WHY DIDN'T YOU INPUT A STRING!?!?!?!")
	return '%s!!!' % txt.upper()

def reverse(txt):
	unable = ['@', '#', '$', '%', '^', '&', '~', ';', '`', ',', '?']
	punctuation = {'!': '!', '*': '*', '(': ')', ')': '(', '_':'_', '-':'-', '+': '+', '=': '=',
				 '{': '}', '}': '{', '[': ']', ']': '[', '\\': '/', '|': '|', '"': '"', ':': ':', 
				 '/': '\\', '>': '<', '<': '>', '.': '.'}
	new_txt = []
	if type(txt) != str:
		raise TypeError("Can only reverse strings!")	
	words = txt.split(" ")
	for word in words:
		try:
			if word in unable:
				raise PunctuationException
		except PunctuationException as inst:
			print inst
		finally: 
			letters = [letter for letter in word]
			letters.reverse()
			for letter in range(len(letters)):
				if letters[letter] in punctuation:
					letters[letter] = punctuation[letters[letter]]
  			new_txt.append(''.join(letters))
  	return ' '.join(new_txt)

def reversewords(txt):
	if type(txt) != str:
		raise TypeError("Can only reverse strings!")
	words = txt.split(" ")
	words.reverse()
	return ' '.join(words)
  
def reversewordletters(txt):
	return reversewords(reverse(txt))
  
def piglatin(txt):
	if type(txt) != str:
		raise TypeError("Can only translate 'ings-stray'")
	vowels = ['a', 'e', 'i', 'o', 'u']
	words = txt.split(" ")
	new_words = []
	for word in words:
		first_vowel = 0
		letters = [letter for letter in word]
		for letter in letters:
			if letter in vowels:
				first_vowel = word.index(letter)
				break
			else:
				continue
		if first_vowel == 0:
			word = '%s-ay' % word
		else:
			word = '%s-%say' % (word[first_vowel:], word[0:first_vowel])
		new_words.append(word)
	return ' '.join(new_words)


