from flask import Flask
from flask import request
from flask import render_template

import forms

from config import DBconfig
from models import db
from models import User



app = Flask(__name__)
db.init_app(app)
app.config.from_object(DBconfig)




@app.route('/', methods=['GET', 'POST'])
def login():
    loginform = forms.formlogin(request.form)
    if request.method == 'POST' and loginform.validate():
        user = User( username=loginform.username.data, password = loginform.password.data)

        db.session.add(user)
        db.session.commit()

    return render_template('login.html', login=loginform)





if __name__ == '__main__':



    with app.app_context():
        db.create_all()

    app.run(port=8888)
