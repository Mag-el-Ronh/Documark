Notizen zur Umsetzung von Markdown in Commonmark.js
====================================================

Offizielle Website: [http://commonmark.org/](http://commonmark.org/)

GitHub von CommonMark: https://github.com/jgm/CommonMark  /  
Github von commonmark.js: https://github.com/jgm/commonmark.js/README.md with link to--> http://spec.commonmark.org/js/commonmark.js  
> src="http://spec.commonmark.org/js/commonmark.js"

MathJax
=======
Integration into
----------------

### HTML
* all MathJax v4 subverions
> <!= script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js">
* for a special subversion number
> <!= script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4.0.0/tex-mml-chtml.js">

### Server installation with Markdown or Latex support 

node.js istallation [ https://www.mathjax.org/#installnow ]
> npm install mathjax

Notepad++
=========

Run Command (F5)
----------------

### HTML - Open in Firefox

> firefox "$(FULL_CURRENT_PATH)"
