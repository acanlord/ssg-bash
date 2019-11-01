#! /usr/bin/python

# Generate HTML content 



filenames = ['./templates/top.html', './content/index.html', './templates/bottom.html'] 
with open('index.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

filenames = ['./templates/top.html', './content/blog.html', './templates/bottom.html'] 
with open('blog.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())


filenames = ['./templates/top.html', './content/projects.html', './templates/bottom.html'] 
with open('projects.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
