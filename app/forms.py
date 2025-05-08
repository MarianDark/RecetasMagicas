from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, TextAreaField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

# Formulario para agregar recetas
class RecipeForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredientes', validators=[DataRequired()])
    preparation = TextAreaField('Preparación', validators=[DataRequired()])
    category = SelectField('Categoría', coerce=int)
    image = FileField('Imagen', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imágenes.')])
    submit = SubmitField('Guardar')

# Formulario de registro
class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

# Formulario de login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')
