from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Mantenha-me conectado')
    submit = SubmitField('Entrar')