#!/usr/bin/python

import sys
from BeautifulSoup import BeautifulSoup

doc = "build/testdoc.html"
#doc=sys.argv[1]

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
    menuItem = "<li " + miClass + miAnchor + "> " + item.text + "</li>"
    #print "full menu item: " + menuItem
    menuHTML += menuItem

#print "HERE'S THE MENU COLLECTOR"
#print menuHTML

file = open("build/menu.txt","w")
file.write("<ul class='menu-ul'>")
for item in menuHTML:
    file.write(item)
file.write("</ul>")
file.close()

finisher = open("build/menu.txt", "r")

file = open("build/menu.html", "w")
for line in finisher:
    temp = line.replace("\'", "\"")
    temp = temp.replace("&&&", "\'")
    file.write(temp)
    print "temp file: " + temp
file.close()

readTemplate = open("templates/template.txt", "r")
file = open("build/index.html", "w")
for line in readTemplate:
    file.write(line)
file.close
