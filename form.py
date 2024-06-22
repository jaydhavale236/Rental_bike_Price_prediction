from calendar import month, weekday
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set a secret key for CSRF protection

class MyForm(FlaskForm):
    Season = StringField('Season', validators=[DataRequired(), Length(min=2, max=20)])
    holiday = StringField('holiday',validators=[DataRequired(), Length(min=2, max=20)])
    workingday = StringField('workingday', validators=[DataRequired(), Length(min=2, max=20)])
    weathersit = StringField('weathersit',validators=[DataRequired(), Length(min=2, max=20)])
    temp = FloatField('temp', validators=[DataRequired(), Length(min=2, max=20)])
    atemp = FloatField('atemp',validators=[DataRequired(), Length(min=2, max=20)])
    humidity = IntegerField('humidity', validators=[DataRequired(), Length(min=2, max=20)])
    windspeed = FloatField('windspeed',validators=[DataRequired(), Length(min=2, max=20)])
    registered = IntegerField('registered', validators=[DataRequired(), Length(min=2, max=20)])
    mnth = IntegerField('mnth', validators=[DataRequired(), Length(min=2, max=20)])
    year = IntegerField('year', validators=[DataRequired(), Length(min=2, max=20)])
    hour = IntegerField('hour', validators=[DataRequired(), Length(min=2, max=20)])
    weekday = IntegerField('weekday', validators=[DataRequired(), Length(min=2, max=20)])
    
    
    
    submit = SubmitField('Submit')

@app.route('/', methods=['POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        flash(f'Hello, {form.name.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)