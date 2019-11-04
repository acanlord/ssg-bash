#! /bin/bash
# Generate new site content


# Clean old files
rm -rf *.html


echo "Were goign to gen your new html files"

# Gen new files
cat templates/top.html content/index.html templates/bottom.html > index.html
cat templates/top.html content/blog.html templates/bottom.html > blog.html
cat templates/top.html content/projects.html templates/bottom.html > projects.html

echo "Build Complete, here's the contents of docs"
ls -l *.html 
open .
