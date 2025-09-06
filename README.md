# Documark
use commonmark and jinja2 in pythto fill a first html docu draft

## requirements

### python libraries from pypi.org

1. commonmark
 > $ pip install commonmark
2.  jinja2
 > $ pip install jinja2


## Reference inforamation from Markdown.pl to modern Commonmark.js

Documark is a python library. For this project is used commonmark (python). Commonmark is a python portation orf reference commonmark.js. commonmarj.js is more consistant and strict than original markdown.pl.
[talk.commonmark.org/t/mistletoe-a-fast-extensible-commonmark-implementation-in-pure-python](https://talk.commonmark.org/t/mistletoe-a-fast-extensible-commonmark-implementation-in-pure-python/2835)

Offizielle Website: [http://commonmark.org/](http://commonmark.org/)

GitHub von CommonMark: https://github.com/jgm/CommonMark  /  
Github von commonmark.js: https://github.com/jgm/commonmark.js/README.md with link to--> http://spec.commonmark.org/js/commonmark.js  
> src="http://spec.commonmark.org/js/commonmark.js"

## MathJax

Latex syntax interpretation in JavaScript of mathematical formula in clean math notation visualisation. 
[latexeditor.lagrida.com/](https://latexeditor.lagrida.com/)

### Integration into HTML

* all MathJax v4 subverions
> <!= script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js">

### Server installation with Markdown or Latex support 

node.js istallation [ https://www.mathjax.org/#installnow ]
> npm install mathjax

### X. Appendix 

* HTML - terminal bash command to show in Firefox:
> firefox "$(FULL_CURRENT_PATH)"
