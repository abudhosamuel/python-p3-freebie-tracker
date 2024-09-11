#!/usr/bin/env python3

# Script goes here!
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = 'companies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    founding_year = db.Column(db.Integer)
    
    freebies = db.relationship('Freebie', backref='company')
    
    @property
    def devs(self):
        return {freebie.dev for freebie in self.freebies}

class Dev(db.Model):
    __tablename__ = 'devs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    freebies = db.relationship('Freebie', backref='dev')
    
    @property
    def companies(self):
        return {freebie.company for freebie in self.freebies}

class Freebie(db.Model):
    __tablename__ = 'freebies'
    
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    dev_id = db.Column(db.Integer, db.ForeignKey('devs.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

    def print_details(self):
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'
