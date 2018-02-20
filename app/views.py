#views.py 

from flask import render_template,redirect, url_for, request,session,flash

from app import app

@app.route("/",methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/home",methods=['GET','POST'])
def about():
    error=None
    if request.method=='POST':
        if request.form['username'] !='username' or request.form['password'] !='password':
            error='Invalid credentials'
        else:
            return redirect(url_for('home'))
    return render_template("index.html",error=error)
    
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
    return render_template("signup.html")

@app.route("/login",methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username'] !='username' or request.form['password'] !='password':
            error='Invalid credentials'
        else:
            return redirect(url_for('/'))
    return render_template("login.html",error=error)

@app.route("/results")
def results():
    return render_template("results.html")