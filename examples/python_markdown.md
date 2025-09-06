# How to use commonmark in scripts
## use python commonmark library as site_package 
python commonmark is ported from original commonmarks.js  javascript

use python virtual env. debugging with python3.13
> conda activate md

install common mark in virtual env
> (md)$ pip install commonmark

## original commonmark.js mit Node.js benutzen um beipiel.md in html umzuwandeln

* Install node.js 
> $ pacman -S nvm 
> $ source /usr/share/nvm/init-nvm.sh 
> $ nvm install --lts 

* neues NodeJs Projekt mit npm anlegen:
> $ mkdir commonmark-projekt 
> $ cd commonmark-projekt 
> $ npm init -y 

* commonmark installieren:
> $ npm install commonmark 

* beispiel.md konvertieren mit konvertiere_beispiel_md2html.j
> $ node konvertiere_beispiel_md2html.js

* generierter HTML-Code wird im Terminal/Console ausgegeben 
