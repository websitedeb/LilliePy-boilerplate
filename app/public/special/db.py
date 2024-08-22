from os import getenv

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient  #uninstall any db you dont want
from redis import Redis
from sqlalchemy.orm import *


class DB():

  def __init__():
    pass  #write your script here


def use_db():
  return DB()
