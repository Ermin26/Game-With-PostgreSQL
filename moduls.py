import os
import psycopg2
from psycopg2 import Error
import dotenv
from dotenv import load_dotenv, find_dotenv
from sqla_wrapper import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

load_dotenv(find_dotenv())

db = SQLAlchemy("DATABASE_URL", 'postgresql://postgres:ermin@localhost:5432/GAME')

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, )
    session_token = db.Column(db.String, )
    secret_number = db.Column(db.Integer, unique=False)
    games = db.Column(db.Integer, )
    wins = db.Column(db.Integer, )
    score = db.Column(db.Integer,)
    losses = db.Column(db.Integer, )
    online = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)


class Message(db.Model):
    __tablename__ = 'message'
    user_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reciver_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    sender = relationship("User", foreign_keys="Message.sender_id")
    reciver = relationship("User", foreign_keys="Message.reciver_id")
