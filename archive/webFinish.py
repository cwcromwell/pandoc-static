#!/usr/bin/python

import sys
import re
import BeautifulSoup

file = sys.argv[1] # contains the html to be inserted between head and footer
out = open(sys.argv[2], 'w') # name of the output file

content = open(file, 'r', encoding = None, errors = 'ignore').read() #renaming file

myTemplate= open (myTemplate.htm. , 'r', encoding=none, errors = 'ignore').read() #the template that content will be inserted insertion

soup = BeautifulSoup(file)

#combine the content with boilerplate parts of the page



for item in stageOne:
    out.write(item)
out.write(content)


for item in stageTwo:
    out.write(item)
