
import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy

import json

database_name = "capstone"
database_path = os.environ.get('DATABASE_URL')


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''

coach
a training coach with a name
and a description a coach can
run many training classes

'''


class Coach(db.Model):
    __tablename__ = 'coach'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    TrainingClasses = db.relationship(
        'TrainingClass', backref='coach',
        cascade="all, delete-orphan",
        lazy='dynamic')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }


'''
TrainingClass
Each Training Class is run by one coach the class
can be allocated on several periods in a day and on
several dayes in a week it also has a name and a
description.

'''


class TrainingClass(db.Model):
    __tablename__ = 'training_class'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    coachId = Column(Integer, db.ForeignKey('coach.id'))
    description = Column(String)
    periods = Column(db.ARRAY(db.String))
    dayes = Column(db.ARRAY(db.String))

    def __init__(self, name, coachId, description, periods, dayes):
        self.name = name
        self.coachId = coachId
        self.periods = periods
        self.dayes = dayes
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'coachId': self.coachId,
            'description': self.description,
            'periods': self.periods,
            'dayes': self.dayes
        }
