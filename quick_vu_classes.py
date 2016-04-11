# Token Mapping
class Page:
	def __init__(self, pageTitle):
		self.pageTitle = pageTitle
		self.pageMarkup = '<html lang="en"> <head> <title>' + self.pageTitle + '</title> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1"> <link rel="stylesheet" href="css/main.css"> <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"> <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script> <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script> </head> <body> <script src="js/script.js"></script> </body> </html>'
	def getMarkup(self):
		""" Here goes logic for returning page"""
	def appendMarkup(self, markup):
		"""	Logic for appending current markup will go here.
			Most likely pyquery will come into action.	"""
	def pagePrettify(self):
		""" Logic for making markup look pretty, not much else to say xD"""
	def pagePackager(self):
		""" Logic in charge of packaging all files into a directory """
	def pagePrint(self):
		"""Logic in charge of printing current page markup"""

class Menu:
	"""docstring for Menu"""
	def __init__(self, type, pageTitle):
		super(Menu, self).__init__()
		self.menuDict = {
			1: '<nav class="navbar navbar-inverse navbar-fixed-top"> <div class="container-fluid"> <div class="navbar-header"> <a class="navbar-brand" href="#">' + pageTitle + '</a> </div> <ul class="nav navbar-nav"> <li class="active"><a href="#">Home</a></li> <li><a href="#">Page 1</a></li> </ul> </div> </nav> <div class="row"></div>',
			2: '<nav class="navbar navbar-inverse navbar-fixed-top"> <div class="container-fluid"> <div class="navbar-header"> <a class="navbar-brand" href="#">' + pageTitle + '</a> </div> <ul class="nav navbar-nav"> <li class="active"><a href="#">Home</a></li> <li><a href="#">Page 1</a></li> </ul> </div> </nav>',
			3: '<nav class="navbar navbar-inverse"> <div class="container-fluid"> <div class="navbar-header"> <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar"> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button> <a class="navbar-brand" href="#">' + pageTitle + '</a> </div> <div class="collapse navbar-collapse" id="myNavbar"> <ul class="nav navbar-nav"> <li class="active"><a href="#">Home</a></li> <li><a href="#">Page 2</a></li> <li><a href="#">Page 3</a></li> </ul> </div> </div> </nav>'
		}
		self.type = self.menuDict[type]

	def getMarkup: 
		""" Logic for returning markup goes here """

	def addPageToMenu:
		"""  Here goes logic for appending a new item to the menu of a site whenever a new page is added """
