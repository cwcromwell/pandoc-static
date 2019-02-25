#!


import sys
import re
import subprocess32

yaml = sys.argv[1] #the yaml file with build instructions
data =  open(yaml, 'r')
docMap = []
newMap = []
outdir = ""
docname = ""
title = ""


#cut lines containing unwanted text string
for line in data:
   if 'href:' in line and '.html' in line:
     #  print line
       docMap.append(line)
   if 'href:' in line and '.md' in line:
      # print line
       docMap.append(line)
   if 'outdir:' in line:
       outdir = line
       outdir = outdir.replace("outdir: ", "")
   if 'Title:' in line:
       title = line
       title = title.replace("Title: ", "")
   if 'Docname:' in line:
       docname = line
       docname = docname.replace("Docname: ", "").rstrip("\n")

   else:
      continue

if docMap:
   print "yaml data collected"
   print(docMap)
else:
    print"No yaml or links not found"

print docname
print title
print outdir


for eachLine in docMap:
    breakLine = eachLine.split(" ")
    for eachPiece in breakLine:
        if 'html' in eachPiece or 'HTML' in eachPiece or 'md' in eachPiece:
            print "line stripper is next"
            newMap.append(eachPiece.rstrip("\n"))

        else:
            continue
#print "Here's the full list:"
#print newMap


outFile = "build/" + docname
out = open(outFile, "w")
outFile = '\"' + outFile + '\",'


docList=" ".join(str(x) for x in newMap)
print "here is the doclist: "
print docList
subprocess32.run(["pandoc", "-f", "markdown", "-t", "html5", "-o", "build/CLItest3.html", docList], input=None, shell=True, stdout=subprocess32.PIPE, stdin=subprocess32.PIPE)

#runCommand = subprocess.Popen(["pandoc", "-f", "markdown", "-t", "html5", "-o", out, docList])
#stdout=subprocess.PIPE
print("runPandoc.py script completed.")
