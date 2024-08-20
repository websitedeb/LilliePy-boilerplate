from flask import flash, redirect, url_for
from flask_login import UserMixin, login_user, logout_user
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash

client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']  #change all of this!
users_collection = db['users']


class User(UserMixin):

  def __init__(self, user_id):
    self.id = user_id


def login_user_auth(email, password):
  user = users_collection.find_one({"email": email})

  if user and check_password_hash(user['password'], password):
    user_obj = User(user['_id'])
    login_user(user_obj)
    flash("Logged in successfully!", "success")
    #add your stuff here
    return redirect(url_for('dashboard'))
  else:
    flash("Invalid credentials", "danger")
    #add your stuff here
    return redirect(url_for('login'))


def logout_user_auth():
  logout_user()
  flash("Logged out successfully!", "success")
  return redirect(url_for('login'))


def register_user(email, password):
  if users_collection.find_one({"email": email}):
    flash("Email already registered", "warning")
    #add your stuff here
  else:
    hashed_password = generate_password_hash(password)
    users_collection.insert_one({"email": email, "password": hashed_password})
    flash("User registered successfully", "success")
    #add your stuff here
    return redirect(url_for('login'))
