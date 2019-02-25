This is the template for a documentation site that uses pandoc to produce HTML from Markdown.

## How to use this tool

### Workflow or creating a single page with a menu

Steps in the build process:

1. Start the virtual Environment like this:

   'source p2nv/bin/activate'

2. Use pandoc to create a continuous, single-page HTML doc. Like this:

   `pandoc -f markdown -t html5 -o build/testdoc.html src/test-doc.md`

   The final item in this command is the input file. You can also use a series of files separated by one space -- without commas.

3. Use the Python script to create a menu for the contents of your html page:

   `menuMaker.py <page_Name.html>`

4. The menu gets manually inserted into the html template to build the full page. The content, however is imported into the template with an html include. It's still necessary to insert the name of the content file into the js script that does that.

(This can all be automated later, but isn't finished yet.)


## More about the components that went into this tool

### About the Virtual Environment

The directory virtualenv contains a Python virtual environment necessary to assemble the packages that make the build work (BeautifulSoup is not compatible with the latest version of Python).

To start the virtual environment:
'source <virtual_environment_name>/bin/activate'

To stop the virtual environment:
`deactivate`

For more about this topic, see the [Python documentation](https://docs.python.org/3.6/tutorial/venv.html).


### About BeautifulSoup

BeautifulSoup parses HTML to grab specified elements. Example:

~~~
>>> from BeautifulSoup import BeautifulSoup

>>> myText=open("build/testdoc.html").read()
>>> soup=BeautifulSoup(myText)
>>> soup("h1")
[]  #There are no H1 elements to be found
>>> soup("h2")
[<h2 id="heading-one">heading one</h2>, <h2 id="heading-two">heading two</h2>, <h2 id="heading-three">heading three</h2>, <h2 id="heading-four">heading four</h2>]

# BeautifulSoup found and returned the array of headings. The text returned is the exact text of the heading (This was a Lorem Ipsum type document).
~~~

### Dependencies

pandoc
p2nv virtual environment
   -BeautifulSoup 3
   -Python 2.7

### Workflow for a new project

0. Use pandoc to build the html version of your content
1. Create the menu by running menumaker.py
2. Make a new folder in pandoc-static and name the project
3. Copy `styles/` and `img/` folders into the new project folder
4. Copy myScript.js to the project folder
5. Copy the template.txt file into the project folder and change the page Name
6. Copy the html file containing the content (from step 0) into the project folder
7. Add the name of the html content file into myScript.js. (line 12)
8. Copy the content of build/menu.html (from step 1) and paste it into the template page in the project (not into the content page) -- it goes in the div marked `id="left-nav"`.
9. Insert the CSS link into the content html page, so that it will be presented properly
