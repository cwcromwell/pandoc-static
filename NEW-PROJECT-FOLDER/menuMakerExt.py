#!/usr/bin/python

import sys
from BeautifulSoup import BeautifulSoup
import os

#collect sys.argv in order to loop through the CONTENTS

corpusList=sys.argv

try:
    os.remove("src/html/menu.txt")
except:
    print "No menu.txt to delete."
try:
    os.remove("src/html/menu.html")
except:
    print "No menu.html to delete."

def menufy( reqItem ):

    doc1 = reqItem.split("/")
    for each in doc1:
        if ".html" in each:
            docName = each
        else:
            continue


    soup = BeautifulSoup(open(reqItem, "r"))
    #print "PRINTING CONTENTS OF DOC:"
    #print soup.prettify()


    menuCollector = soup.findAll(['h1', 'h2', 'h3'])
    print "NOW MENUFYING:"
    print reqItem

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


    file = open("src/html/menu.txt","a")
    file.write(" <!-- This is the beginning of the generated menu --> ")
    for item in menuHTML:
        file.write(item)
    file.write("<!-- This is the end of the generated menu -->")
    file.close()


for item in corpusList:
    if "menuMaker" in item:
       continue
    else:
        menufy(item)

finisher = open("src/html/menu.txt", "r")

file = open("src/html/menu.html", "w")
for line in finisher:
    temp = line.replace("\'", "\"")
    temp = temp.replace("&&&", "\'")
    file.write(temp)
    print "temp file: " + temp
file.write("<!-- end of menu.html -->")
file.close()
