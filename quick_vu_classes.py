# Page Classes

# Importing PyQuery Library for html management
from pyquery import PyQuery as pq

# Importing BeautifulSoup Library for cleaning final html output
from bs4 import BeautifulSoup
		

class Page(object):
	def __init__(self, pageTitle):
		super(Page, self).__init__()
		self.pageTitle = pageTitle
		self.markup = '<html lang="en"> <head> <title>' + self.pageTitle + '</title> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1"> <link rel="stylesheet" href="css/main.css"> <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"> <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script> <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script> </head> <body> <script src="js/script.js"></script> </body> </html>'
		self.d = pq(self.markup)

	def getMarkup(self):
		return self.markup

	def getPrettyMarkup(self):
		""" Here goes logic for returning page"""
		soup = BeautifulSoup(self.markup, 'html.parser')
		return soup.prettify()

	def appendMarkup(self, markup):
		"""	Logic for appending current page body markup with parameter markup.	"""
		self.d('body').append(markup)

	def pagePackager(self):
		""" Logic in charge of packaging all files into a directory """

	def pagePrint(self):
		"""Logic in charge of printing current page markup"""
		print(self.getPrettyMarkup())

class Menu(object):
	"""docstring for Menu"""
	def __init__(self, type, pageTitle):
		super(Menu, self).__init__()
		self.menuDict = {
			1: '<nav class="navbar navbar-inverse navbar-fixed-top"> <div class="container-fluid"> <div class="navbar-header"> <a class="navbar-brand" href="#">' + pageTitle + '</a> </div> <ul class="nav navbar-nav"> <li class="active"><a href="#">Home</a></li> <li><a href="#">Page 1</a></li> </ul> </div> </nav> <div class="row"></div>',
			2: '<nav class="navbar navbar-inverse navbar-fixed-top"> <div class="container-fluid"> <div class="navbar-header"> <a class="navbar-brand" href="#">' + pageTitle + '</a> </div> <ul class="nav navbar-nav"> <li class="active"><a href="#">Home</a></li> <li><a href="#">Page 1</a></li> </ul> </div> </nav>',
			3: '<nav class="navbar navbar-inverse"> <div class="container-fluid"> <div class="navbar-header"> <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar"> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button> <a class="navbar-brand" href="#">' + pageTitle + '</a> </div> <div class="collapse navbar-collapse" id="myNavbar"> <ul class="nav navbar-nav"> <li class="active"><a href="#">Home</a></li> <li><a href="#">Page 2</a></li> <li><a href="#">Page 3</a></li> </ul> </div> </div> </nav>'
		}

		self.markup = self.menuDict[type]
		self.d = pq(self.markup)

	def getMarkup(self):
		return self.markup

	def getPrettyMarkup(self):
		""" Here goes logic for returning page"""
		soup = BeautifulSoup(self.markup, 'html.parser')
		return soup.prettify()

	def addPageToMenu(self, pageTitle):
		"""  Here goes logic for appending a new item to the menu of a site whenever a new page is added """
		self.d('ul').append('<li><a href="#">' + pageTitle + '</a></li>')

