#!/usr/bin/python

import sys

doc = sys.argv[1]
docOne = ""

docIn = doc.split("/")
for item in docIn:
    if ".html" in item:
        docOut = item


fromFile = open(doc,"r").read()
tempA = open("templates/templateA.html", "r").read()
tempB = open("templates/templateB.html", "r").read()
menu = open("src/html-src/menu.html", "r").read()


for line in tempA:
    if "iframe" in line:
        print "iframe found in tempA"
        continue
    else:
        docOne = docOne + line
for line in menu:
    if "iframe" in line:
        print "iframe found in menu"
        continue
    else:
        docOne = docOne + line
for line in fromFile:
    if "iframe" in line:
        print "iframe found in fromFile"
        continue
    else:
        docOne = docOne + line
for line in tempB:
    if "iframe" in line:
        print "iframe found in tempB"
        continue
    else:
        docOne = docOne + line

# print docOne

out = "build/" + docOut
toFile = open(out,"w")
toFile.write(docOne)
