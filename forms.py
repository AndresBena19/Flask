from wtforms import Form
from wtforms import StringField, TextField


from wtforms import validators


class  formlogin(Form):
    username= StringField('user', [validators.Required(message='falta campo'), validators.length(min=1, max=100)])
    password= StringField('password', [validators.Required(message='falta campo'), validators.length(min=1, max=100)])
