from flask import Flask, render_template, flash, redirect, url_for, request
from dbmodel import Data
from db import db
import pandas as pd
from sqlalchemy.exc import OperationalError
import os
from flask_migrate import Migrate
from cachedData import redis_client


app = Flask(__name__)
app.secret_key = "Secret key"

# Set the database connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost/webappdb'

# Disable tracking modifications to reduce overhead
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

print("Connecting to database:", app.config['SQLALCHEMY_DATABASE_URI'])

# Function to upload data from CSV
def upload_data_from_csv():
    csv_path = 'csv/tests.csv'
    
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        for index, row in df.iterrows():
            my_data = Data(
                vehicleid=row['vehicleid'],
                timestamp=row['timestamp'],
                coordinate_longitude=row['coordinate_longitude'],
                coordinate_latitude=row['coordinate_latitude'],
                event_description=row['event_description'],
                speed=row['speed'],
                heading=row['heading'],
                ignitionState=row['ignitionState'],
                gps_accuracy=row['gps_accuracy'],
                gps_fix_type=row['gps_fix_type']
            )
            db.session.add(my_data)
            db.session.commit()

        # Move the CSV file to the "processed" folder after processing
        processed_folder = 'processed'
        if not os.path.exists(processed_folder):
            os.makedirs(processed_folder)
        
        new_csv_path = os.path.join(processed_folder, 'tests.csv')
        os.rename(csv_path, new_csv_path)
        
    else:
        print("CSV file not available.")

# Function to clear cached data in Redis
def clear_cached_data():
    redis_client.delete('cached_data')

@app.route('/')
def Index():
    cached_data = redis_client.get('catched_data')
    if cached_data:
        all_data = eval(cached_data.decode())
    else:
        all_data = Data.query.all()
        redis_client.set('cached_data', repr(all_data))
    return render_template("index.html", vehicles=all_data)

@app.route('/insert', methods=['POST'])
def insert():
    try:
        if request.method == 'POST':
            vehicleid = request.form['vehicleid']
            timestamp = request.form['timestamp']
            coordinate_longitude = request.form['coordinate_longitude']
            coordinate_latitude = request.form['coordinate_latitude']
            event_description = request.form['event_description']
            speed = request.form['speed']
            heading = request.form['heading']
            ignitionState = request.form['ignitionState']
            gps_accuracy = request.form['gps_accuracy']
            gps_fix_type = request.form['gps_fix_type']

            my_data = Data(
                vehicleid=vehicleid,
                timestamp=timestamp,
                coordinate_longitude=coordinate_longitude,
                coordinate_latitude=coordinate_latitude,
                event_description=event_description,
                speed=speed,
                heading=heading,
                ignitionState=ignitionState,
                gps_accuracy=gps_accuracy,
                gps_fix_type=gps_fix_type
            )
            db.session.add(my_data)
            db.session.commit()
            
            flash("Vehicle Added Successfully")
            clear_cached_data()

    except OperationalError as e:
        db.session.rollback()  # Rollback the transaction
        flash(f"An error occurred on {e} while adding the vehicle. Please check your input.")

    return redirect(url_for('Index'))

@app.route('/map')
def map_view():
    all_data = Data.query.all()  # Fetch all vehicle data
    return render_template("map.html", vehicles=all_data)
    
@app.route('/update', methods=['POST'])
def update():
    try:
        if request.method == 'POST':
            id = request.form['id']
            vehicleid = request.form['vehicleid']
            timestamp = request.form['timestamp']
            coordinate_longitude = request.form['coordinate_longitude']
            coordinate_latitude = request.form['coordinate_latitude']
            event_description = request.form['event_description']
            speed = request.form['speed']
            heading = request.form['heading']
            ignitionState = request.form['ignitionState']
            gps_accuracy = request.form['gps_accuracy']
            gps_fix_type = request.form['gps_fix_type']
            
            my_data = db.session.query(Data).get(id)
            if my_data:
                my_data.vehicleid = vehicleid
                my_data.timestamp = timestamp
                my_data.coordinate_longitude = coordinate_longitude
                my_data.coordinate_latitude = coordinate_latitude
                my_data.event_description = event_description
                my_data.speed = speed
                my_data.heading = heading
                my_data.ignitionState = ignitionState
                my_data.gps_accuracy = gps_accuracy
                my_data.gps_fix_type = gps_fix_type
                
                db.session.commit()
                flash("Vehicle Updated Successfully")
                clear_cached_data()

    except OperationalError as e:
        db.session.rollback()  # Rollback the transaction
        flash(f"An error occurred on {e} while updating the vehicle record. Please check your input.")

    return redirect(url_for('Index'))
            
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = db.session.query(Data).get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash(f"Vehicle for this Vehicle ID {my_data.vehicleid} Deleted Successfully")
    clear_cached_data()
    return redirect(url_for('Index'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the table if it doesn't exist
        upload_data_from_csv()  # Upload data from CSV
    app.run(debug=True)
