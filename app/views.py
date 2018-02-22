#views.py 

from flask import render_template,redirect, url_for, request,session,flash
#from functools import wraps 
from app import app

app.secret_key="my precious"

#def login_required(f):
#    @wraps(f)
#    def wrap(*args, **kwargs):
#        if 'logged_in' in session:
#            return f(*args, **kwargs)
#        else:
#            flash('You need to login first.')
#            return redirect(url_for('login'))
#    return wrap

@app.route("/")
def about():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")
    
@app.route("/registerbusiness", methods=['GET','POST'])
def registerbusiness():
    error=None
    if request.method=='POST':
        if request.form['business'] !='simba' or request.form['location'] !='kampala':
            error='Invalid credentials'
        else:
            return redirect(url_for('mybusinesses'))
    return render_template("registerbusiness.html",error=error)

@app.route("/mybusinesses", methods=['GET', 'POST'])
def mybusinesses():
    return render_template("mybusinesses.html")

@app.route("/signup")
def signup():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return render_template("signup.html")

@app.route("/login",methods=['GET','POST'])
def login():
    error=None
    session.pop('logged_in', None)
    
    if request.method=='POST':
        if request.form['username'] !='admin' or request.form['password'] !='admin':
            error='Invalid credentials'
        else:
            session['logged in']=True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template("login.html",error=error)

@app.route("/results")
def results():
    return render_template("results.html")






