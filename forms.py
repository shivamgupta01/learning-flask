from flask_wtf import Form
from wtforms import PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired,Email, Length

class SignupForm(Form):
    first_name = StringField('First Name',validators=[DataRequired("Please Enter your First Name")])
    last_name = StringField('Last Name', validators=[DataRequired("Please Enter your Last Name")])
    email = StringField('Email', validators=[DataRequired("Please Enter your Email"),Email("Enter Valid Email ID")])
    password = PasswordField('Password', validators=[DataRequired("Please Enter your Password"),Length(min=6,message="Password should be more than 6 characters")])
    submit = SubmitField('Sign Up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please Enter your Email"),Email("Enter Valid Email ID")])
    password = PasswordField('Password', validators=[DataRequired("Please Enter your Password"),Length(min=6,message="Password should be more than 6 characters")])
    submit = SubmitField('Sign in')

class AddressForm(Form):
    address = StringField('Address', validators=[DataRequired("Please enter an Address")])
    submit = SubmitField('Search')
