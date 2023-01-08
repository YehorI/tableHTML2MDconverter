import itertools
import re
from bs4 import BeautifulSoup, ResultSet, element

def remove_whitespace_characters(text):
    altered_text = text.replace('\t', ' ').replace('\n', ' ').replace('\xa0', ' ').replace('\r', ' ').replace('&nbsp;', '')
    altered_text = re.sub(r' +', ' ', altered_text)
    return altered_text

def tables_from_html(page: str) -> ResultSet:
    soup = BeautifulSoup(page, 'html.parser')
    return soup('table')


def html2markdowntable(table: element.Tag) -> str:
    '''
    INPUT: soup.table
    OUTPUT: markdowntable | 1 | 2 |
                          |---|---|
                          | 3 | 4 |
    '''
    parsed_table = []
    if table.thead:
        for tr in table.thead('tr'):
            parsed_table.append([])
            for td in tr(['th', 'td']):
                parsed_table[-1].append(
                    remove_whitespace_characters(td.get_text())
                    )

    if table.tbody:
        for tr in table.tbody('tr'):
            parsed_table.append([])
            for td in tr('td'):
                parsed_table[-1].append(
                    remove_whitespace_characters(td.get_text())
                    )

    table_data_sizes = [len(parsed_table[0][i]) for i in range(len(parsed_table[0]))]

    for tr in parsed_table[1:]:
        for _, td in enumerate(tr):
            max_size = table_data_sizes[_]
            table_data_sizes[_] = max_size if len(td) < max_size else len(td)
    table_title = f'''|{
        ''.join([
            ''.join([
                td,
                ' ' * (table_data_sizes[_] - len(td)),'|'
                ]) for _, td in enumerate(parsed_table[0])
            ])
        }\n{
    ''.join(['|', *['-' * i + '|' for i in table_data_sizes]])
    }\n'''

    table_content = []
    for tr in parsed_table[1:]:
        table_content.append(
            f'''|{
                ''.join([
                    ''.join([
                        td,
                        ' ' * (table_data_sizes[_] - len(td)),'|'
                        ]) for _, td in enumerate(tr)
                    ])
                }\n'''
            )

    markdown_table = ''.join([table_title, *table_content])
    return markdown_table

def main():
    with open('example.html', encoding='utf-8') as fp:
        tables = tables_from_html(fp.read())

    markdown_tables = []

    for table in tables:
        markdown_tables.append(html2markdowntable(table))

    with open('output.txt', 'w', encoding='utf-8') as f:
        for markdown_table in markdown_tables:
            f.write(markdown_table)
            f.write('\n')

if __name__ == '__main__':
    main()