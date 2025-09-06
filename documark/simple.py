#-*-coding:utf8;-*-

import os
import sys

if len(sys.argv) > 1:
    input_file_name =sys.argv[1]
else:
    print("need input file name with markdown content")
    input_file_name = [ "commonmark_notes.md" ]

import commonmark
parser = commonmark.Parser()

'''read markdown example file content '''
with open(input_file_name, 'r', encoding='utf-8') as test_note_file:
    test_note = test_note_file.read()
    test_note_file.close()

'''convert example content in markdown format to html format'''
ast = parser.parse(test_note)
renderer = commonmark.HtmlRenderer()
html = renderer.render(ast)
print(html)

output_file_name = f'{input_file_name[:-3]}.html'
with open(output_file_name, 'w', encoding='utf-8') as html_out_file:
    html_out_file.write(html)
    html_out_file.close()
print(f'Converted markdown input was writen into output file "{output_file_name}".')
