# to run this in emacs start the python interpreter via C -c C -p then C -c C -c
import string
import textwrap
import re

gkbooklist = []


def main():
	# for writing to a global declare it as global first
	global gkbooklist
	with open('gk-dickens.txt') as text_file:
		gkbooklist = text_file.readlines()
	stringstuff()


def stringstuff():
	s = 'The quick brown fox jumped over the lazy brown dog.'
	print (string.capwords(s))	
	templates()
	prettyprinting()
	regulars()


def templates():
	# ---------------templates-----------------
	# this is a map
	values = {"iamakey":"iamavalue"}
	t = string.Template("""
	Here is some stuff: $iamakey
	""")
	print (t.substitute(values))


def prettyprinting():
	booksample = ""
	# we can refer to a global variable here, if just accessing it, no special syntax required
	for line in gkbooklist[550:560]:
		# this will get rid of all the newlines
		booksample += textwrap.dedent(line)
	print (booksample)


def regulars():
	wholebook = "".join(gkbooklist)
	print('---------- Regular Expressions -----------------')
	copperfield_pattern = 'calvinistic'
	for match in re.findall(copperfield_pattern, wholebook, re.IGNORECASE):
		print(match)
	print('----------------------------')
	index = 0
	for match in re.finditer(copperfield_pattern, wholebook, re.IGNORECASE):
		s = match.start()
		e = match.end()
		print('------------------------------')
		print(index + 1)
		print(wholebook[s: e + 200])
		index += 1
		
main()
