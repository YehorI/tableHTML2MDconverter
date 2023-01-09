from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class GetHTML(FlaskForm):

    input_type = SelectField(
        'Откуда вы хотите получить таблицы',
        coerce = int,
        choices = [
            (0, 'ссылка'),
            (1, 'HTML-файл'),
            (2, 'текст')
        ]
    )
    html_file = FileField(
        'Прикрепите файл',
        validators=[FileAllowed(['html', 'txt'])]
        )
    text_window = TextAreaField('Текст', render_kw={'cols':'100', 'rows':'20'})
    submit = SubmitField('Отправить')

