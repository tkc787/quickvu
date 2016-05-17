# -----------------------------------------------------------------------------
# QuickVU.py
#
# A lexical analyzer to make html.
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"../..")


# Global Variables

# Counter variable holding 0 if a page instance has not been created
global cc 
c = {'c': 0}

from intermidiate import Page
x = Page()

if sys.version_info[0] >= 3:
	raw_input = input

tokens = (
	'NAME',
	'LANK',
	'RANK',
	'ACTION',
	'ELEMENTS',
	'NUM',
	'WS',
	)

# Tokens

t_NAME        = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ELEMENTS 	  = r'\d+|paragraph|form|textarea|text|dropdown|input|radio|checkbox|submit|list|button|number'
t_ACTION	  = r'vucreate|vumenu|vuelement|vuform|vufooter|vufinish'
# t_LPAR		  = r'\('
# t_RPAR 		  = r'\)'
t_LANK		  = r'\<'
t_RANK 		  = r'\>'
t_WS 		  = r' [ ]+ '
t_ignore 	  = "\t\n"

def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t
	
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)
	
# Build the lexer
import ply.lex as lex
lex.lex()

def p_statements(p):
	'''
	statements : 
			   | statements statement
	'''

def p_statement(p):
	'''statement : LANK ACTION parameters RANK
				 | LANK ACTION RANK
				 | WS LANK ACTION parameters RANK
				 | WS LANK ACTION RANK'''

	if str(p[1]).isspace():
		i = 3
	else:
		i = 2
	if p[i] == 'vucreate':
		try:
			if c['c'] == 0:
				x.startPage(p[i+1])
				c['c'] += 1
			else:
				print(x.getPageTitle() + ' page instance is already running, use vufinish command before starting new instance')
		except AttributeError:
			print("No page has been initialized, first use VUcreate command to initiate page")
	elif p[i] == 'vumenu':
		try:
			x.addMenu(p[i+1])
		except AttributeError:
			print("No page has been initialized, first use VUcreate command to initiate page")		
	elif p[i] == 'vuelement':
		try:
			x.addContent(p[i+1])
		except AttributeError:
			print("No page has been initialized, first use VUcreate command to initiate page")		
	elif p[i] == 'vuform':
		try:
			x.addFormElement(p[i+1])
		except AttributeError:
			print("No page has been initialized, first use VUcreate command to initiate page")
	# elif p[1] == 'VUfooter':
	# 	x.addFooter()
	elif p[i] == 'vufinish':
		try:
			x.addFooter()
			x.pagePackager()
			c['c'] -= 1
			print("HTML has been generated successfully!")
		except AttributeError, e:
			print(str(e))
			print("No page has been initialized, first use VUcreate command to initiate page")
	else:
		print("Syntax Error, Action statement not valid!")

# parameters: '(' element ')'
def p_parameters(p):
	'''parameters : WS ELEMENTS
				  | WS NUM
				  | WS NAME
				  '''
	p[0] = p[2]

def p_error(p):
	if p:
		print("Syntax error at '%s'" % p.value)
	else:
		print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()
		
while 1:
	try:
		s = raw_input('QuickVu > ')
	except EOFError:
		break
	if not s: continue
	yacc.parse(s)
	
# with open(filename) as f:
	# for line in f.readlines():
		# do_something(line)
# with open('test.txt') as f:		
# 	for line in f:
# 		try:
# 			s = line
# 			print(s)
# 		except EOFError:
# 			break
# 		if not s:
# 			continue
# 			yacc.parse(s)
