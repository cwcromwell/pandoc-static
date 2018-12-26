This is the template for a documentation site that uses pandoc to produce HTML from Markdown.

More instructions to come.


## About the Virtual Environment

The directory virtualenv contains a Python virtual environment necessary to assemble the packages that make the build work (BeautifulSoup is not compatible with the latest version of Python).

To start the virtual environment:
'source virtualenv/bin/activate'

To stop the virtual environment:
`deactivate`

For more about this topic, see the [Python documentation](https://docs.python.org/3.6/tutorial/venv.html).


## About BeautifulSoup

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
