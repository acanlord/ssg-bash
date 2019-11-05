#! /usr/bin/python

import os

# Generate HTML content 

print("Were going to gen your new html content")

filenames = ['./templates/top.html', './content/index.html', './templates/bottom.html'] 
with open('./docs/index.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

filenames = ['./templates/top.html', './content/blog.html', './templates/bottom.html'] 
with open('./docs/blog.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())


filenames = ['./templates/top.html', './content/projects.html', './templates/bottom.html'] 
with open('./docs/projects.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

print("Were all done, Here's your files\n")

for root, dirs, files in os.walk("./docs"):
    for filename in files:
        print(filename)
