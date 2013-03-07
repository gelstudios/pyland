#qsort

def	qsort(some_string):
	"""returns a sorted string"""
	letters=[]
	for s in some_string:
		letters.append(s)
	letters.sort()
	qsort_output=''.join(letters)
	return qsort_output

def xplod(some_string, delimeter):
	""""explodes a string into a list"""
	elements = []
	for s in some_string:
		elements.append(s)
	return elements
	