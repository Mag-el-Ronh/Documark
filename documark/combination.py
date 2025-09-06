import os
from datetime import date
from jinja2 import Environment, PackageLoader, select_autoescape
from documark import deprecated

env = Environment(
    loader=PackageLoader("documark"),
    autoescape=select_autoescape())

template_base = env.get_template("base.html") 
template_header = env.get_template("header.html") 
template_md_article = env.get_template("md_article.html") 

class docu_properties:
    ''' 
    property to fill jinja template documark/templates/header.html
    @param author: name of author of last changes
    @param update_date: date when laste changes were done
    '''

    @property
    def author(self):
        return self._author
        
    @author.getter
    def author(self):
        return str(self._author)
    
    @author.setter
    def author(self, name):
        if name != None:
            self._author = name
        else:
            self._author = os.getlogin()
        
    @property
    def update_date(self):
        return self._update_date
        
    @update_date.getter
    def update_date(self):
        return str(self._update_date)
        
    @update_date.setter
    def update_date(self, value):
        if value != None:
            value = date.today()
        self._update_date=str(value)
       
def createHeader(docu = None, **kargs):
    ''' @depricated:
        because variable {{ header }} is not used.
        instead replaced by {% include "header.html" %} in "base.html"
    '''
    if docu == None:
        docu = docu_properties
        docu.author=None
        docu.update_time=None

    _D = {"author": docu.author,
          "update_date": docu.update_date}
    _D.update(kargs)
    return _D
    
    #_header = template_header.render(**_D)
    #return _header

def MD2HtmlArticle(content):
    '''
    extend html format string into <article>content</article>
    @param content:article html content 
    @returns: article tag with included content in html format
    '''
    content = f' <article>\n{content}\n <\\article\n>'
    print(f'# acticle is \n=============== \n {content}')
    return(content)    

@deprecated
def oldMD2HtmlArticle(content):
    '''
    convert string in markdown format into html of templates/md_article.html
    @param md_content: markdown input file content which has to be converted 
        to fill html article with content
    '''
    
    md_article = template_md_article.render(**_D)
    print(f'md acticle content = \n=============== \n {md_article}')
    return md_article

def createHtml(header, articles ):
    '''
    @param header: docu_properties() obj with attributes of "author and
        "update_date" 
    @param articles: list  of string arguments, 
        each arg contains one article content
    '''
    a = ""
    _D = { "author": header.author,
           "update_date": header.update_date,
           #"articles": "".join([a.join(a_x) for a_x in articles])
           "articles": "".join("".join(articles))
           }
    _html = template_base.render(**_D)
    return _html

