#! /usr/bin/python

# Generate HTML content 



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
