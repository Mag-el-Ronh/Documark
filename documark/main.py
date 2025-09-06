#-*-coding:utf8;-*-

import os
import sys
sys.path.extend(os.path.realpath("~/Entwicklung/freelancer"))
from documark import combination

input_file_names= list()
print(f'sys.argv = {sys.argv}')
if len(sys.argv) > 1:
    input_file_names.extend(sys.argv[1:])
else:
    print("need input file name with markdown content")
    input_file_names.extend(os.path.join(os.getcwd(),"commonmark_notes.md"))
input_file_names = [ os.path.join(os.getcwd(),i_f_n) for i_f_n in input_file_names ]
print(f'#input_file_names = {input_file_names}')

import commonmark
parser = commonmark.Parser()

def readMardownArticleFile(file_name):
    '''read markdown example file content '''
    with open(file_name, 'r', encoding='utf-8') as md_file:
        md_note = md_file.read()
        md_file.close()
    return md_note

def convertArticle(md_content):
    ''' use commonmark library to convert string 
    @param md_content: string in md format
    @returns: converted html string
    '''
    ast = parser.parse(md_content)
    renderer = commonmark.HtmlRenderer()
    _html = renderer.render(ast)
    return _html

header = combination.docu_properties()
header.author = None
header.update_date = None

# list of article_files.md
if type(input_file_names) != list:
    a_content = readMardownArticleFile(input_file_names)
    articles = list(combination.MD2HtmlArticle(a_content))
else:
    articles = list()
    for inp_f in input_file_names:
        print(f' md file to convert = {inp_f}')
        _a = readMardownArticleFile(inp_f)
        #print(f' read md file contend = {_a}')
        _content = convertArticle(_a)
        #print(f'## article_content = {_content}')
        a_content = combination.MD2HtmlArticle(_content)
        articles.extend(a_content)
html = combination.createHtml(header, articles)

output_file_name = f'{input_file_names[0][:-2]}html'
with open(output_file_name, 'w', encoding='utf-8') as html_out_file:
    html_out_file.write(html)
    html_out_file.close()

