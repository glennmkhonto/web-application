from db import db
from sqlalchemy import String, TIMESTAMP, DECIMAL, Integer

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicleid = db.Column(String(10))
    timestamp = db.Column(TIMESTAMP)
    coordinate_longitude = db.Column(DECIMAL(10, 6))
    coordinate_latitude = db.Column(DECIMAL(10, 6))
    event_description = db.Column(String(255))
    speed = db.Column(Integer)
    heading = db.Column(Integer)
    ignitionState = db.Column(String(3))  
    gps_accuracy = db.Column(Integer)
    gps_fix_type = db.Column(Integer)  



