from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Flight {self.origin} {self.destination}>'

class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
    
    def __repr__(self):
        return f'<Passenger {self.id} {self.name}>'
    
    