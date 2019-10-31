#! /bin/bash



#cd ssg-bash
#git pull.sh


#cat top.html index.html bottom.html > docs/index.html


cat templates/top.html content/index.html templates/bottom.html > index.html
cat templates/top.html content/blog.html templates/bottom.html > blog.html
cat templates/top.html content/projects.html templates/bottom.html > projects.html

echo "Build Complete, here's the contents of docs"
ls -l .


#git add -a
#git commit -m "updated stuff" 
#git push
