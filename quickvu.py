# -----------------------------------------------------------------------------
# QuickVU.py
#
# A lexical analyzer to make html.
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"../..")

# Global Variables
from classes import Page
x = Page()

if sys.version_info[0] >= 3:
	raw_input = input

tokens = (
	'NAME',
	'LPAR',
	'RPAR',
	'ACTION',
	'ELEMENTS',
	'NUM',
	)

# Tokens

t_NAME        = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ELEMENTS 	  = r'\d+|paragraph|form|text|dropdown|input|radio|checkbox|submit|list|button|textarea|number'
t_ACTION	  = r'VUcreate|VUmenu|VUelement|VUform|VUfooter|VUfinish'
t_LPAR		  = r'\('
t_RPAR 		  = r'\)'
# t_COMMA 	  = r','

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

def p_statement(p):
	'''statement : ACTION parameters
				 | ACTION'''
	if p[1] == 'VUcreate':
		try:
			x.startPage(p[2])
		except AttributeError:
			print("No page has been initialized, first use VUcreate command to initiate page")
		p[0] = p[2]
	elif p[1] == 'VUmenu':
		try:
			x.addMenu(p[2])
		except AttributeError:
			print("No page has been initialized, first use VUcreate command to initiate page")		
		p[0] = p[2]
	elif p[1] == 'VUimport':
# 		Enter Import code here
		p[0] = p[2]	
	elif p[1] == 'VUelement':
		try:
			x.addContent(p[2])
		except AttributeError:
			print("No page has been initialized, first use VUcreate command to initiate page")		
		p[0] = p[2]
	elif p[1] == 'VUform':
		try:
			x.addFormElement(p[2])
		except AttributeError:
			print("No page has been initialized, first use VUcreate command to initiate page")
		p[0] = p[2]
	# elif p[1] == 'VUfooter':
	# 	x.addFooter()
	elif p[1] == 'VUfinish':
		try:
			x.addFooter()
			x.pagePackager()
		except AttributeError:
			print("No page has been initialized, first use VUcreate command to initiate page")		
		print("HTML has been generated successfully!")
	else:
		print("Syntax Error, Action statement not valid!")
		p[0] = 'Syntax Error'

# parameters: '(' element ')'
def p_parameters(p):
	'''parameters : LPAR RPAR
				  | LPAR ELEMENTS RPAR
				  | LPAR NUM RPAR
				  | LPAR NAME RPAR
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
		s = raw_input('QuickVU > ')
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
