# Getting Started


## The Basic Workflow

* run menuMakerExt.py  against all the pages to produce a full menu
* run splicer.py against individual pages of content, to put each page together with the header, footer, and menu
*

## Set Up Your Project

Follow These Steps to Create a New Site with Your Documents:

1. Copy source files into the `/src` directory.
2. Create a non-executable text file where you can store your build commands. They contain long lists of files and you won't want to type them in every time you build. It's easier to add a filename every time you create a new file.


## Build Your PROJECT

1. Start the virtual Environment like this:

   'source p2nv/bin/activate'

   The menuMaker script will not run without the virtual environment.

2. Use pandoc to convert individual markdown pages to a single-page HTML doc. Like this:

   `pandoc -f markdown -t html5 -o src/html/testdoc.html src/test-doc.md`

   The final item in this command is the input file. You can also use a series of files separated by one space, without commas, if you want to combine several markdown pages into a single html page.

3. Use the Python script to create a menu for the contents of all your html pages. The entire site will have one menu, so all the pages need to go into this command. Like so:

  `menuMakerExt.py  <page_Name.html> <page_Name_2.html> <page_Name_3.html>`

Pages are named with a relative path from the directory where you run the buildscript.

4. Use the Splicer to join your new content page with the header, footer, and menu. Like this:

  `./splicer.py <filename.html>`

You currently have to convert one file at a time, because each of them is a separate HTML page. This could be scripted in the future.
