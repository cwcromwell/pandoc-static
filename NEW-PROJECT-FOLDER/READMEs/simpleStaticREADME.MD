
# Read me

This is the readme file for the NEW-PROJECT-FOLDER. Previous versions of READMEs are saved in a subfolder here.

## Contents

These topics are covered.

* dependencies (including the virtual environment)
* contents of this folder

## Requirements and Dependencies

### Dependencies

If the following dependencies aren't installed, all bets are off:

* pandoc
* p2nv virtual environment
     - BeautifulSoup 3
     - Python 2.7

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

## Contents of the project folders

The project folder is set up to quickly build a clone of the askme project, one that works in the same way. It contains templates, CSS, and sample content that you can use to build a site approximately the same as the askme web site.

You don't need the images and content, but including them in the file structure makes it easy to substitute another file in their place, and that's what most people do when they adapt a project for their own use.

More useful are the python scripts that build the HTML menu and then the web pages from your markdown.

Here's a manifest of what is included in the folder, and what each file does:

Name | Description
----------|--------------------
`menuMakerExt.py` | Use it to build the kind of HTML menu that users expect to see on a documentation site. For instructions, see the Quickstart.
`splicer.py` | Assembles your content, the menu and a header and footer into a web page.
`src/html` | HTML pages go here after Pandoc converts them from markdown, but before they are combined together into the final site. The content you see here won't be publishable. Also the folder where the menu gets built by the menuMakerExt.py script.
`deliverables` | Contains everything necessary to the final site. When ready to publish, you should copy this folder and push it to your remote repo on the web server. And don't put anything here that should not be public.
`deliverables/img`| Any images that will be included in the final site should go here. Link to them like this: `../img/<image_name>`.
`deliverables/syles` | Contains CSS necessary for the functionality of the site.
`deliverables/js` | Contains any JavaScript incorporated into the final site. Link to them from the index.html page like this: `js/<script_name>`. And from other pages like this: `../js/<script_name>`.
`deliverables/pages` | Build scripts will dump the completed html pages here, for inclusion in the final version of the site.
