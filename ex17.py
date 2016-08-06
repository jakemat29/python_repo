def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(stuff):
	"""this function will sort words in a string"""
	words = sorted(stuff)
	return words
	
def print_first_word(stuff):
	"""this fn pops the 1st letter in the split words"""
	word = stuff.pop(1)	# instead of pop(1) if it is pop(-1) it prints the last word
	print word
	
print "enter a sentence"
input = raw_input(">")

sent = input  #'input' variable just keeps the original string 
spl = break_words(sent)
print "The broke up words from a string :::\n %r" %spl


sorted = sort_words(spl)		#the split words are passed into sort_words fn
print "The sorted words from a string :::\n %r" %sorted

print "the popped one from the slitted one \n "
print_first_word(spl)
