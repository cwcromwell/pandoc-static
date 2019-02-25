import subprocess32
subprocess32.run(["pandoc", "-f", "markdown", "-t", "html5", "-o", "build/myCLItest.html", "src/test-doc.md"])
