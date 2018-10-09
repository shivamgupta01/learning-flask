from flask import Flask, render_template, request, session, redirect, url_for
from models import db,User,Place
from forms import SignupForm,LoginForm, AddressForm
from flask import request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)

app.secret_key = 'development-key'

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route('/signup',methods = ['GET','POST'])
def signup():
  if 'email' in session:
      return redirect(url_for('home'))
  form = SignupForm()
  if request.method == 'POST':
    if form.validate() == False:
      print("Form validation Failed")
      return render_template('signup.html',form = form)
    else:    
      newuser = User(form.first_name.data,form.last_name.data,form.email.data,form.password.data)
      db.session.add(newuser)
      db.session.commit()
      session['email'] = newuser.email
      return redirect(url_for('home'))
  else:  return render_template('signup.html',form = form)

@app.route('/home', methods = ['GET','POST'])
def home():
  if 'email' not in session:
    return redirect(url_for('login'))
  form = AddressForm()
  my_coordinates = []
  places = (37.4221,-122.0844)
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('home',form = form)
    else:
      
      # Get The Address
      address = form.address.data
      # Query the places Around it
      p = Place()
      my_coordinates = p.address_to_latlng(address)
      places = p.query(address)
      # Show the Results
      return render_template('home.html',form = form,my_coordinates = my_coordinates,places = places)

  return render_template('home.html',form = form,my_coordinates = my_coordinates,places = places)

@app.route('/login',methods = ['GET','POST'])
def login():
  if 'email' in session:
    return redirect(url_for('home'))
  form = LoginForm()
  if request.method == 'POST':
    if form.validate() == False:
      print("Form validation Failed")
      return render_template('login.html',form = form)

    else:    
      email = form.email.data
      password = form.password.data
      user = User.query.filter_by(email = email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data
        return redirect(url_for('home'))
      else:
        return redirect(url_for('login'))
  else:  return render_template('login.html',form = form)

@app.route('/logout')
def logout():
  session.pop('email',None)
  return redirect(url_for('index'))

if __name__ == "__main__":
  app.run(debug=True)