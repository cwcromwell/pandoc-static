#!/usr/bin/python

import sys
from BeautifulSoup import BeautifulSoup




doc = sys.argv[1]
#doc=sys.argv[1]

doc1 = doc.split("/")
for item in doc1:
    if ".html" in item:
        docName = item
    else:
        continue


soup = BeautifulSoup(open(doc, "r"))
#print "PRINTING CONTENTS OF DOC:"
#print soup.prettify()


menuCollector = soup.findAll(['h1', 'h2', 'h3'])

print "COLLECTING ALL HEADINGS"
#print menuCollector

print "BUILDING MENU"
menuHTML = ""
# set numerical value and class, to control menu nesting and styles
for item in menuCollector:
    miAnchor = " onclick='changer(&&&"+ item.attrs[0][1] + "&&&)'"
    #print "anchor is: " + miAnchor
    miClass = "class='menu-" + item.name + "'"
    #print "miClass is: " + miClass
    menuItem = "<li " + miClass + miAnchor + "><a href=\'" + docName +"#" + item.attrs[0][1] + "\'>" + item.text + "</a></li>"
    #print "full menu item: " + menuItem
    # <a href="taketwo.html#groups" >
    menuHTML += menuItem

#print "HERE'S THE MENU COLLECTOR"
#print menuHTML


file = open("src/html-src/menu.txt","w")
file.write(" <div id='left-nav' > <ul class='menu-ul'>")
for item in menuHTML:
    file.write(item)
file.write("</ul></div>")
file.close()

finisher = open("src/html-src/menu.txt", "r")

file = open("src/html-src/menu.html", "w")
for line in finisher:
    temp = line.replace("\'", "\"")
    temp = temp.replace("&&&", "\'")
    file.write(temp)
    print "temp file: " + temp
file.write("</div>")
file.close()
