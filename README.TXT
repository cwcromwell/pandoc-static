This is the template for a documentation site that uses pandoc to produce HTML from Markdown.

## How to use this tool

### Workflow

Steps in the build process:

1. Start the virtual Environment like this:

   'source p2nv/bin/activate'

2. Use pandoc to create a continuous, single-page HTML doc. Like this:

   `pandoc -f markdown -t html5 src/test-doc.md -o build/testdoc.html`

3. Use the Python script to create a menu for the contents of your html page:

   `menuMaker.py <page_Name.html>`

4. The menu gets inserted in the template.



You don't have to do anything further to make the output work.

* In the template, *an iframe loads the content** which is at the top of the menu
* Also in the template, **a script loads the menu**



## More about the components that went into this tool

### About the Virtual Environment

The directory virtualenv contains a Python virtual environment necessary to assemble the packages that make the build work (BeautifulSoup is not compatible with the latest version of Python).

To start the virtual environment:
'source virtualenv/bin/activate'

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
   -BeautifulSoup
   -Python 2.7
<<<<<<< HEAD
=======
   
>>>>>>> 3c76dfc9f174311021dc3cd3cd8066f0a0c5a2f2
