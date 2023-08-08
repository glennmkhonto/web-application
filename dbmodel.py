from db import db
from sqlalchemy import String, TIMESTAMP, DECIMAL, Integer

#db = SQLAlchemy()

# class Data(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     phone = db.Column(db.String(100))

#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicleid = db.Column(String(10))
    timestamp = db.Column(TIMESTAMP)
    coordinate_longitude = db.Column(DECIMAL(10, 6))
    coordinate_latitude = db.Column(DECIMAL(10, 6))
    event_description = db.Column(String(255))
    speed = db.Column(Integer)
    heading = db.Column(Integer)
    ignitionState = db.Column(String(3))  # Adjust type as needed
    gps_accuracy = db.Column(Integer)
    gps_fix_type = db.Column(Integer)  # Adjust type as needed



