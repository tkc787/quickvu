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
	'COMMA',
	'ACTION',
	'ELEMENTS',
	'NUM',
	)

# Tokens

t_NAME        = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ELEMENTS 	  = r'\d+|paragraph|form|text|dropdown|input|radio|checkbox|submit|list|button|textarea|number'
t_ACTION	  = r'VUcreate|VUmenu|VUcontainer|VUform|VUfooter'
t_LPAR		  = r'\('
t_RPAR 		  = r'\)'
# t_VUCREATE    = r'VUcreate'
# t_VUMENU      = r'VUmenu'
# t_VUFOOTER    = r'VUfooter'
# t_VUCONTAINER = r'VUcontainer'
# t_PARAGRAPH	  = r'paragraph'
# t_FORM        = r'form'
# t_TEXT        = r'text'
# t_DROPDOWN    = r'dropdown'
# t_INPUT       = r'input'
# t_RADIO       = r'radio'
# t_CHECKBOX    = r'checkbox'
# t_SUBMIT      = r'submit'
# t_LIST        = r'list'
# t_BUTTON      = r'button'
# t_TEXTAREA    = r'textarea'
# t_NUMBER      = r'number'

def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_COMMA(t):
	r','
	t.lexer.skip(1)

# def t_newline(t):
# 	r'\n+'
# 	return t
	
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)
	
# Build the lexer
import ply.lex as lex
lex.lex()

def VUcrear(elements):
	y = elements[:]
	x.startPage(y[3]) 					
	return "Page has been created."
	
def VUmenuar(elements):
	y = elements[:]
	x.addMenu(y[3], x.getPageTitle)
	return "Menu has been created."
	
def VUcontenear(elements):
	y = elements[:]
	k = []
	for z in y:
		if z in keywords.values():
			k.append(z)
			
	x.addContent(k)
	return "Container has been created."
		
def VUfootear(elements):
	y = elements[:]
	x.addFooter(y[3])
	return "Footer has been created."
	
methods_ops = {
	"VUcreate"    : VUcrear,
	"VUmenu"      : VUmenuar,
	"VUfooter"    : VUfootear,
	"VUcontainer" : VUcontenear
}

# keywords = {
# 	"paragraph" : t_PARAGRAPH,
# 	"form" 		: t_FORM,
# 	"text"      : t_TEXT,
# 	"dropdown" 	: t_DROPDOWN, 
# 	"input" 	: t_INPUT,
# 	"list" 		: t_LIST,
# 	"button" 	: t_BUTTON,
# 	"radio"     : t_RADIO,
# 	"checkbox"  : t_CHECKBOX,
# 	"submit"    : t_SUBMIT,
# 	"textarea"	: t_TEXTAREA,
# 	"number"	: t_NUMBER
# }

# def p_expression_op(p):
# 	"expression : expression '(' expression ')'"
# 	elements = p[:]
# 	print(p)
# 	p[0] = methods_ops[p[1]](elements)

# funcdef: [decorators] 'def' NAME parameters ':' suite
# ignoring decorators

# dictionary of names
names = { }

def p_statement(p):
	"statement : ACTION parameters"
	if p[1] == 'VUcreate':
		print('fuck you')
	else: 
		p[0] = p[2]


# def p_statement_assign(p):
#     'statement : NAME "=" ACTION'
#     names[p[1]] = p[3]

# def p_statement_expr(p):
#     'statement : expression'
#     print(p[1])

# parameters: '(' [varargslist] ')'
def p_parameters(p):
	"""parameters : LPAR RPAR
				  | LPAR varargslist RPAR"""
	print(p)
	if len(p) == 3:
		p[0] = []
	else:
		p[0] = p[2]

# varargslist: (fpdef ['=' test] ',')* ('*' NAME [',' '**' NAME] | '**' NAME) | 
# highly simplified
def p_varargslist(p):
	"""varargslist : varargslist COMMA ELEMENTS
				   | ELEMENTS
				   | NUM
				   | NAME
				   """
	if len(p) == 4:
		p[0] = p[1] + p[3]
	else:
		p[0] = [p[1]]

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
