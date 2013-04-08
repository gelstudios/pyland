import re

session = []
def logprint(msg, list):
	"""Prints the log message and appends it to a given list
	
	Lists must be initialized at the module level.
	"""
	print(msg)
	list.append(msg)

def logsave(list, filename):
	"""Saves the list to a given filename"""
	f = open(filename, "a")
	f.write('\n')
	f.write('\n'.join(list))
	f.close()
	
def inquire(prompt, response, contains):
	"""a
	"""
	knock = None
	while knock == None:
		logprint(prompt, session)
		user_input = raw_input(">")
		knock = re.search(contains, user_input)
		if knock == None:
			logprint(response, session)
	return user_input

def main():
	inquire("::You are at someone's door::\n", "**crickets**\n", '[kK]nock')
	stuff = inquire("Who's there?\n", "**blank stare**\n", '.+')
	stuff = inquire(stuff + " who?\n", "**glaring at you**\n", '.+')
	logprint(stuff + "!?, that's hilarious!\n", session)
	logsave(session, "knockknock.txt")

if __name__ == '__main__':
	main()