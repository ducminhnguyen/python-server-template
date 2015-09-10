import sass

def compileScss():
	print "Compiling SCSS"
	scssFolder = "./views/static/scss"
	cssFolder = "./views/static/css"
	sass.compile(dirname=(scssFolder, cssFolder), source_comment=True)
	