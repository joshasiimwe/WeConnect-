#app/__init__.py 
from flask import Flask,render_template, redirect, url_for, request,session,flash
from functools import wraps
#initialise the app

app = Flask(__name__, instance_relative_config=True)

#load the views

from app import views 

#load the config file

app.config.from_object("config")