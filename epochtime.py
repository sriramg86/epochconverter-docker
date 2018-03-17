from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, IntegerField
import time

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'abcde7578'
 
class ReusableForm(Form):
    epochtime = IntegerField('Epoch Time : ', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    if request.method == 'POST':
        epochtime=request.form['epochtime']
        print(epochtime)
 
        if form.validate():
            timeconv=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(epochtime)))
            flash(timeconv)
        else:
            flash('Error: Enter Epoch time in proper format')
 
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5400)