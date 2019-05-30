import PyPDF2
from tkinter import * 
from tkinter import filedialog
import os
import subprocess, platform
from tkinter import messagebox

currDir = os.getcwd()
root = Tk()
root.withdraw()

root.filename = filedialog.askopenfilename(initialdir='/', title="Select file", filetypes = (("pdf files","*.pdf"),("all files","*.*")))

if(root.filename == ''):
	exit()

outFileName = root.filename[0:-4] + "out.pdf"

print(outFileName)

readPDF = PyPDF2.PdfFileReader(root.filename)
writePDF = PyPDF2.PdfFileWriter()

for i in range(readPDF.getNumPages()):
	page = readPDF.getPage(i)
	ll = page.cropBox.getLowerLeft()
	ul = page.cropBox.getUpperLeft()
	lr = page.cropBox.getLowerRight()
	ur = page.cropBox.getUpperRight()

	#0.03270223752 is the factor of the added watermark to the page height

	page.cropBox.lowerLeft = (ll[0], ll[1] + ul[1]*0.03270223752)
	page.cropBox.lowerRight = (lr[0], lr[1] + ur[1]*0.03270223752)


	writePDF.addPage(page)

with open(outFileName, "wb") as out_f:
   	writePDF.write(out_f)



if platform.system() == 'Darwin':
	subprocess.call(('open', outFileName))
elif platform.system() == 'Windows':  
    os.startfile(outFileName)
else:                                   
    subprocess.call(('xdg-open', outFileName))


