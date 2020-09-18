"""
stanCode SC101 Assignment 5 Problem 5
File: boggle.py
Name: Tiffany Lin
----------------------------------------
This file simulates the word game, boggle.
Users input letters into a 4X4 tray with the format
in which words are separated by space
and only english letters are allowed -- case insensitive.
Once all letters are entered, the game begins
and all words in sequences of adjacent letters
will be found and printed.
The number of words found will be shown in the end.
"""

# Constants
FILE = 'dictionary.txt'		  # This is the file name of the dictionary txt file

# Global Variables
dictionary = []               # A list containing all the vocabs in the dictionary
word = ''  					  # A str saving the letters in the process of forming the word
keys = []    				  # A list saving the index of letters when constructing the word
n = 0						  # An int counting the number of words found
found = []					  # A list of all words found and printed


def main():
	"""
	User input 4X4 letters and all words
	in sequences of adjacent letters
	will be found and printed.
	"""
	boggle_grid = {}
	game = ''

	# Input letters on boggle grid and save them in a list
	for i in range(4):
		r = (str(input(f"{i+1} row of letters: ")))
		r = r.lower()
		if len(r) != 7 or r[1] != ' ' or r[3] != ' ' or r[5] != ' ' or not_all_alpha(r):
			print('Illegal input')
			game = 'ended'
			break
		else:
			r = r.split()
			for j in range(4):
				letter = r.pop(0)
				boggle_grid[(i, j)] = letter

	# Once boggle grid is set, start finding words
	if game != 'ended':
		read_dictionary()
		find_words(boggle_grid)
		print(f"There are {n} words in total.")


def find_words(b):
	"""
	:param b: The dictionary saving all the letters on boggle grid
	:return: (str) Word constructed from the letters of sequentially adjacent ones
	"""
	for x in range(4):
		for y in range(4):
			first_letter = (x, y)
			loop_words(b, first_letter, b[first_letter])


def loop_words(b, current_key, current_value):
	"""
	:param b: A dictionary saving all the letters on boggle grid
	:param current_key: A list saving the index of letters used
	:param current_value: A str saving the letters when constructing words
	:return: Word constructed
	"""
	global word, n, found

	if len(word) >= 4:
		if word in dictionary:
			if word not in found:
				print(f"Found \"{word}\"")
				n += 1
				found.append(word)
				recursive_loop(b, current_key, current_value)
	else:
		recursive_loop(b, current_key, current_value)


def recursive_loop(b, current_key, current_value):
	"""
	:param b: A dictionary saving all the letters on boggle grid
	:param current_key: A list saving the index of letters used
	:param current_value: A str saving the letters when constructing words
	:return: Word constructed
	"""
	global word
	# Choose
	w = word
	word += current_value
	keys.append(current_key)

	# Explore
	if has_prefix(word):
		(x, y) = current_key
		# Upper left
		if 1 <= x <= 3 and 1 <= y <= 3:
			if (x-1, y-1) not in keys:
				loop_words(b, (x-1, y-1), b[(x-1, y-1)])
		# Above
		if 1 <= x <= 3 and 0 <= y <= 3:
			if (x-1, y) not in keys:
				loop_words(b, (x-1, y), b[(x-1, y)])
		# Upper right
		if 1 <= x <= 3 and 0 <= y <= 2:
			if (x-1, y+1) not in keys:
				loop_words(b, (x-1, y+1), b[(x-1, y+1)])
		# Left
		if 0 <= x <= 3 and 1 <= y <= 3:
			if (x, y-1) not in keys:
				loop_words(b, (x, y-1), b[(x, y-1)])
		# Right
		if 0 <= x <= 3 and 0 <= y <= 2:
			if (x, y+1) not in keys:
				loop_words(b, (x, y+1), b[(x, y+1)])
		# Lower left
		if 0 <= x <= 2 and 1 <= y <= 3:
			if (x+1, y-1) not in keys:
				loop_words(b, (x+1, y-1), b[(x+1, y-1)])
		# Below
		if 0 <= x <= 2 and 0 <= y <= 3:
			if (x+1, y) not in keys:
				loop_words(b, (x+1, y), b[(x+1, y)])
		# Lower right
		if 0 <= x <= 2 and 0 <= y <= 2:
			if (x+1, y+1) not in keys:
				loop_words(b, (x+1, y+1), b[(x+1, y+1)])

	# Un-choose
	word = w
	keys.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list.
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for w in f:
			w = w.strip()
			dictionary.append(w)
	return dictionary


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global dictionary
	t = 0
	for w in dictionary:
		if w.startswith(sub_s) is True:
			t += 1
	if t > 0:
		return True


def not_all_alpha(r):
	"""
	:param r: (str) User's input
	:return: (bool) Whether user's input are all letters and no punctuation marks
	"""
	a = 0
	for ch in [r[0], r[2], r[4], r[6]]:
		if not ch.isalpha():
			a += 1
	if a > 0:
		return True


if __name__ == '__main__':
	main()
