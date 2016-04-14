# Page Classes



# Import module for prettifying HTML
from html5print import HTMLBeautifier

# Importing PyQuery Library for html management
from pyquery import PyQuery as pq

# Importing BeautifulSoup Library for cleaning final html output
from bs4 import BeautifulSoup
		
# class BaseMarkup(object):
#     __metaclass__  = abc.ABCMeta

#     @abstractmethod
# 	def getMarkup(self):
# 		""" Return current Object Markup """
		
# 	@abstractmethod
# 	def getPrettyMarkup(self):
# 	""" Logic for returning page with correct html indentation """

# 	@abstractmethod
# 	def appendMarkup(self, markup, node):
# 	""" Logic for appending markup to target node """

class Page:
	def startPage(self, pageTitle):
		self.pageTitle = pageTitle
		self.head = '<!DOCTYPE html> <html lang="en"> <head> <title>' + self.pageTitle + '</title> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1"> <link rel="stylesheet" href="css/main.css"> <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"> <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script> <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script> </head>'
		self.markup = '<body style="padding-top: 70px;"> <div class="container"> <div class="row"> <div class="col-sm-3"> </div> <div id="main" class="col-sm-6"> <h2 class="text-center">Main column</h2> </div> <div class="col-sm-3"> </div> </div> </div> </body>'
		self.d = pq(self.markup)
		self.hasMenu = False
		self.hasFooter = False
		self.hasForm = False
		self.form = None

	def getMarkup(self):
		""" Return object markup string """
		return self.markup

	def getPrettyMarkup(self):
		""" Here goes logic for returning page markup string, with correct indentation """
		# soup = BeautifulSoup(self.markup, 'html5lib')
		return HTMLBeautifier.beautify(self.markup, 4)

	def appendMarkup(self, markup, node):
		"""	Logic for appending current page body markup with parameter markup.	"""
		self.d(node).append(markup)

	def getPageTitle(self):
		return self.pageTitle

	def addMenu(self, type):
		if not self.hasMenu:
			m = Menu(type, self.pageTitle)
			self.d('body').prepend(m.getMarkup())
			self.markup = self.d('body')
			self.hasMenu = True
		else:
			print('Page already has a menu.')

	def addContent(self, element):
		if element == 'paragraph':
			self.appendMarkup(Content.addParagraph(), '#main')
		elif element == 'list':
			self.appendMarkup(Content.addList(), '#main')
		elif element == 'button':
			self.appendMarkup(Content.addButton(), '#main')
		self.markup = self.d('body')

	def addFormElement(self, element):
		if not self.hasForm:
			self.hasForm = True
			self.form = Form()
			self.appendMarkup(self.form.getMarkup(), '#main')

		else:
			newElement = ""

			if element == 'textarea':
				newElement = self.form.addTextArea()
			elif element == 'dropdown':
				newElement = self.form.addDropdown()
			elif element == 'checkbox':
				newElement = self.form.addCheckbox()
			elif element == 'radio':
				newElement = self.form.addRadio()
			elif element == 'text':
				newElement = self.form.addTextInput()
			elif element == 'password':
				newElement = self.form.addPasswordInput()
			elif element == 'number':
				newElement = self.form.addNumberInput()
			elif element == 'submit':
				newElement = self.form.addSubmit()

			self.appendMarkup(newElement, 'fieldset')

	def addFooter(self):
		""" Logic for adding a footer to the page """
		if not self.hasFooter:
			f = Footer()
			self.d('body').append(f.getMarkup())
			self.markup = self.d('body')
			self.hasFooter = True
		else:
			print('Page already has a footer.')

	def pagePackager(self):
		""" Logic in charge of packaging all files into a directory """
		print(self.markup)
		f = open(self.pageTitle + '.html', 'w+')
		f.write(self.head + str(self.markup) + '</html>')
		f.close()

	def pagePrint(self):
		"""Logic in charge of printing current page markup"""
		print(self.getPrettyMarkup())

class Menu:
	def __init__(self, type, pageTitle):
		# super(Menu, self).__init__()
		self.menuDict = {
			1: '<nav class="navbar navbar-inverse navbar-fixed-top"> <div class="container-fluid"> <div class="navbar-header"> <a class="navbar-brand" href="#">' + pageTitle + '</a> </div> <ul class="nav navbar-nav"> <li class="active"><a href="#">Home</a></li> <li><a href="#">Page 1</a></li> </ul> </div> </nav>',
			2: '<nav class="navbar navbar-inverse navbar-fixed-top"> <div class="container-fluid"> <div class="navbar-header"> <a class="navbar-brand" href="#">' + pageTitle + '</a> </div> <ul class="nav navbar-nav"> <li class="active"><a href="#">Home</a></li> <li><a href="#">Page 1</a></li> </ul> </div> </nav>',
			3: '<nav class="navbar navbar-inverse"> <div class="container-fluid"> <div class="navbar-header"> <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar"> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button> <a class="navbar-brand" href="#">' + pageTitle + '</a> </div> <div class="collapse navbar-collapse" id="myNavbar"> <ul class="nav navbar-nav"> <li class="active"><a href="#">Home</a></li> <li><a href="#">Page 2</a></li> <li><a href="#">Page 3</a></li> </ul> </div> </div> </nav>'
		}

		self.markup = self.menuDict[type]
		self.d = pq(self.markup)

	def getMarkup(self):
		return self.markup

	def getPrettyMarkup(self):
		""" Here goes logic for returning page"""
		# soup = BeautifulSoup(self.markup, 'html5lib')
		return HTMLBeautifier.beautify(self.markup, 4)

	def addPageToMenu(self, pageTitle):
		""" Here goes logic for appending a new item to the menu of a site whenever a new page is added """
		self.d('ul').append('<li><a href="#">' + pageTitle + '</a></li>')

class Form:
	def __init__(self):
		self.markup = '<form role="form"> <fieldset class="form-group"> </fieldset> </form>'
		self.d = pq(self.markup)

	def getMarkup(self):
		""" Return object markup string """
		return self.markup

	def getPrettyMarkup(self):
		""" Here goes logic for returning page markup string, with correct indentation """
		# soup = BeautifulSoup(self.markup, 'html5lib')
		return HTMLBeautifier.beautify(self.markup, 4)

	def appendMarkup(self, markup, node):
		"""	Logic for appending current page body markup with parameter markup.	"""
		self.d(node).append(markup)

	def addTextArea(self):
		""" Logic for adding a textarea to the form """
		return '<div class="form-group"> <label for="textBox">Text area label:</label> <textarea class="form-control" placeholder="Write in your textarea" id="textBox"></textarea> </div>'

	def addDropdown(self):
		"""	Logic for adding a dropdown to the form	"""
		return '<div class="form-group"> <label for="sel1">Select list:</label> <select class="form-control" id="sel1"> <option>for every option</option> </select> </div>'

	def addCheckbox(self):
		"""	Logic for adding a checkbox to the form	"""
		return '<div class="checkbox"> <label><input type="checkbox" value="">Checkbox</label> </div>'

	def addRadio(self):
		"""	Logic for adding a radio button to the form	"""
		return '<div class="radio"> <label><input type="radio">Radio button</label> </div>'

	def addTextInput(self):
		""" Logic in charge of adding an input form element """
		return '<div class="form-group"> <label for="theInput">Text Input:</label> <input type="text" class="form-control" id="theInput"> </div>'

	def addPasswordInput(self):
		""" Logic in charge of adding an input form element """
		return '<div class="form-group"> <label for="theInput">Password Input:</label> <input type="password" class="form-control" id="theInput"> </div>'

	def addNumberInput(self):
		""" Logic in charge of adding an input form element """
		return '<div class="form-group"> <label for="theInput">Number Input:</label> <input type="number" class="form-control" id="theInput"> </div>'

	def addSubmit(self):
		"""	Logic for adding a submit button to the form """
		return '<button type="submit" class="btn btn-default">Submit</button>'

class Content:

	def getMarkup(self):
		""" Return object markup string """
		return self.markup

	def getPrettyMarkup(self):
		""" Here goes logic for returning page markup string, with correct indentation """
		# soup = BeautifulSoup(self.markup, 'html5lib')
		return HTMLBeautifier.beautify(self.markup, 4)

	def appendMarkup(self, markup, node):
		"""	Logic for appending current page body markup with parameter markup.	"""
		self.d(node).append(markup)

	@staticmethod
	def addParagraph():
		"""	Logic for adding a paragraph """
		return '<p>This is a paragraph. Write blocks of text here.</p>'

	@staticmethod
	def addList():
		"""	Logic for adding a list """
		return '<ul class="list-group"> <li class="list-group-item">this is a list item</li> </ul>'

	@staticmethod
	def addButton():
		"""	Logic for adding a button """
		return '<button type="button" class="btn btn-default">A button</button>'

class Footer:
	def __init__(self):
		self.markup = '<div class="navbar navbar-inverse navbar-fixed-bottom" role="navigation"><div class="container"><div class="navbar-text pull-left">HTML generated by QuickVu!</div></div></div>'
		self.d = pq(self.markup)

	def getMarkup(self):
		""" Return object markup string """
		return self.markup

	def getPrettyMarkup(self):
		""" Here goes logic for returning page markup string, with correct indentation """
		# soup = BeautifulSoup(self.markup, 'html5lib')
		return HTMLBeautifier.beautify(self.markup, 4)

	def appendMarkup(self, markup, node):
		"""	Logic for appending current page body markup with parameter markup.	"""
		self.d(node).append(markup)
