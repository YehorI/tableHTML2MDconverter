import os
import requests
from flask import Flask, render_template, redirect, url_for, request
from forms import GetHTML
from werkzeug.utils import secure_filename
import html2md_table
from config import SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'uploaded files')
app.config['MAX_CONTENT_PATH'] = 50_000 # in bytes


@app.route('/', methods=['GET', 'POST'])
def index():
    form = GetHTML()
    markdown_tables = []

    if request.method == 'POST' and form.validate_on_submit():

        # LINK
        if form.input_type.data == 0:
            r = requests.get(form.text_window.data)
            tables = html2md_table.tables_from_html(r.text)
            for table in tables:
                markdown_table = html2md_table.html2markdowntable(table)
                markdown_tables.append(markdown_table)

        # HTML
        if form.input_type.data == 1:
            page = request.files['html_file']
            # filename = secure_filename(page.filename)
            # page.save(os.path.join(app.instance_path, 'uploaded files', filename))
            tables = html2md_table.tables_from_html(page)
            for table in tables:
                markdown_table = html2md_table.html2markdowntable(table)
                markdown_tables.append(markdown_table)

        # TEXT
        if form.input_type.data == 2:
            tables = html2md_table.tables_from_html(form.text_window.data)
            for table in tables:
                markdown_table = html2md_table.html2markdowntable(table)
                markdown_tables.append(markdown_table)
        return render_template('index.html', form=form, markdown_tables=markdown_tables)
    else:
        return render_template('index.html', form=form, markdown_tables=markdown_tables)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)