import sys
import re

header1 = re.compile(r'#\s*(.*)')
header2 = re.compile(r'##\s*(.*)')
header3 = re.compile(r'###\s*(.*)')
bold = re.compile(r'\*\*\s*([^\*]+)\s*\*\*')
italic = re.compile(r'\*\s*([^\*]+)\s*\*')
orderedList = re.compile(r'\d+\.\s+(?P<item>.*)', re.MULTILINE)
link = re.compile(r'[^!]\[(?P<nomeLink>.*)\]\((?P<link>.*)\)')
image = re.compile(r'!\[(?P<nomeImagem>.*)\]\((?P<linkImagem>.*)\)')

markdown_input = ""
for line in sys.stdin:
    markdown_input += line

output = markdown_input
output = re.sub(header3, r'<h3>\1</h3>', output)
output = re.sub(header2, r'<h2>\1</h2>', output)
output = re.sub(header1, r'<h1>\1</h1>', output)
output = re.sub(bold, r'<b>\1</b>', output)
output = re.sub(italic, r'<em>\1</em>', output)


def process_ordered_list_lines(text):
    lines = text.splitlines()
    result = []
    in_list = False
    list_items = []

    for line in lines:
        m = re.match(orderedList, line)
        if m:
            list_items.append(f'<li>{m.group("item")}</li>')
            in_list = True
        else:
            if in_list:
                result.append('<ol>' + ''.join(list_items) + '</ol>')
                list_items = []
                in_list = False
            result.append(line)

    # if the text ended while still in a list, close it
    if in_list:
        result.append('<ol>' + ''.join(list_items) + '</ol>')

    return "\n".join(result)


output = process_ordered_list_lines(output)
output = re.sub(link, r' <a href="\g<link>">\g<nomeLink></a>', output)
output = re.sub(
    image, r'<img src="\g<linkImagem>" alt="\g<nomeImagem>"/>', output)


print(output)
