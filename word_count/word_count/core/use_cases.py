
BAG_OF_GARBAGE = [',', ';', '.', ':', '?', '^', '~', '{', '}', '[', ']', '/', '\\', '`', '\'', '"']

def count_words_use_case(words):

	zero_spaces = words.split()

	for garbage in BAG_OF_GARBAGE:
		while garbage in zero_spaces:
			zero_spaces.remove(garbage)

	words_number = len(zero_spaces)
	return words_number