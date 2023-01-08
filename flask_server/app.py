import requests
from flask import Flask, render_template
from forms import GetHTML
import html2md_table.html2md_table as html2md_table

from bs4 import BeautifulSoup, ResultSet, element

app = Flask(__name__)
app.secret_key = 'my_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = GetHTML()
    if form.validate_on_submit():
        markdown_tables = []
        if form.input_type.data == 0: # link
            r = requests.get(form.text_window.data)
            tables = html2md_table.tables_from_html(r.text)
            for table in tables:
                markdown_table = html2md_table.html2markdowntable(table)
                markdown_tables.append(markdown_table)
        if form.input_type.data == 1: # html
            pass
        if form.input_type.data == 2: # text
            tables = html2md_table.tables_from_html(form.text_window.data)
            for table in tables:
                markdown_table = html2md_table.html2markdowntable(table)
                markdown_tables.append(markdown_table)
        return render_template('index.html', form=form, markdown_tables=markdown_tables)
    else:
        return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)