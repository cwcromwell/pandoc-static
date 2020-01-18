# CLI Clipboard

These are cut-and-paste commands that can be used as-is to build the demo project. No modification is necessary, if you follow the Quickstart instructions and use the files provided with this folder.

## Start the virtual Environment

   'source p2nv/bin/activate'

##  Convert markdown pages to HTML

There are two files, so you have to run the command once for each.

~~~
$   pandoc -f markdown -t html5 -o src/html/src/html/resources.html src/resources.html

[. . .]

$   pandoc -f markdown -t html5 -o src/html/src/html/what-is-APIdoc.html src/what-is-APIdoc.html

[. . .]

~~~

## Create a menu for the site

~~~
./menuMakerExt.py src/html/resources.html src/html/what-is-APIdoc.html src/html/announcements.html

~~~

## Create final pages that include menu, contents, header and footer

~~~
$ ./splicer.py src/html/resources.html

$ ./splicer.py src/html/what-is-APIdoc.html
~~~
