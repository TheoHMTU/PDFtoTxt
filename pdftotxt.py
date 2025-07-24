# Creator: Théo Holzhausen


import pdfreader, sys, os
from pdfreader import PDFDocument, SimplePDFViewer

if len(sys.argv) < 2:
    print("No files selected to convert! Exiting program...")

# Extracts an individual page and adds it to the given output file
def extractPage(pageNum, viewer, outF):
    try:
        viewer.navigate(pageNum)
    except:
        return "No page"
    viewer.render()
    strings = viewer.canvas.strings
    outF.write(''.join(strings))
    return "page"


# Takes an int and converts the PDF file at the command line in that position and creates a txt file with its output
# INPUT: command-line number
# OUTPUT: A new txt file of the same name as the PDF file
def convertFile(num):
    if os.path.isfile(sys.argv[num]) != True:
        print(sys.argv[num] + " could not be opened!")
        return None
    filenameArr = sys.argv[num].split(".")
    filename = filenameArr[0]
    print(filename + " is being processed...", end = " ")
    inF = open(sys.argv[num], "rb")
    outF = open(filename + ".txt", "w")
    viewer = SimplePDFViewer(inF)
    # viewer = SimplePDFViewer(inF)
    x = 1
    ret = ""
    
    while ret != "No page":
        ret = extractPage(x, viewer, outF)
        x += 1
    
    inF.close()
    outF.close()
    del viewer
    print("Done!")

for i in range(1, len(sys.argv)):
    convertFile(i)
