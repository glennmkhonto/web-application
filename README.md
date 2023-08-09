# web-application

The Vehicle Tracking Web Application is a Flask-based web application that allows users to manage and visualize vehicle data using an interactive map. This README provides information on the app's design, database model, and instructions for launching the app.

# Application Design

The application follows a client-server architecture with the following key components:

    Frontend: The frontend is built using HTML, Bootstrap for styling, and Jinja2 templating for dynamic rendering of data.

    Backend: The backend is implemented using Flask, a Python web framework. It handles routes, database interactions, and rendering templates.

    Database: The app uses a MySQL database to store vehicle data. The SQLAlchemy ORM is employed to interact with the database.

    Map Visualization: The Leaflet.js library is used for interactive map visualization, with vehicle markers representing location data.

# Database Model

The application's database model consists of a single table named Data, which includes the following fields:

    id (Primary Key): Auto-incremented unique identifier for each record.
    vehicleid: The ID of the vehicle.
    timestamp: Timestamp of the data entry.
    coordinate_longitude: Longitude coordinate of the vehicle's location.
    coordinate_latitude: Latitude coordinate of the vehicle's location.
    event_description: Description of the event associated with the data.
    speed: Speed of the vehicle.
    heading: Heading direction of the vehicle.
    ignitionState: Ignition state of the vehicle.
    gps_accuracy: GPS accuracy.
    gps_fix_type: GPS fix type.

# Launching the Application

Follow these steps to launch the Vehicle Tracking Web App:

1) Clone the Repository:

git clone https://github.com/glennmkhonto/web-application.git

cd web-application

2) Install Dependencies:

pip install -r requirements.txt

3) Configure Database:

    Open app.py and update the SQLALCHEMY_DATABASE_URI in the app.config section to your database connection string.

4) CSV Data Upload:

    Place your CSV file in the csv folder at the root of the project directory.

    Run the Flask app to upload data from the CSV file into the database:

    python app.py

    The CSV file will be moved to the processed folder after processing.

Run the App:

python app.py

Access the App:

    Open your web browser and navigate to http://localhost:5000.
    You can manage and visualize vehicle data using the provided web interface.

# Funtionality

    View Map:
        To view the vehicle data on a map, click on the "View Map" link in the navigation menu.

    Manage Vehicle Data:
        You can manage vehicle data by adding, updating, and deleting records.
        To add a new vehicle, click the "Add New Vehicle" button and fill in the details.
        To update a vehicle's information, click the "Edit" button next to the respective record.
        To delete a vehicle's record, click the "DELETE" button next to the respective record. A confirmation dialog will appear, then click "ok" if happy to proceed.

# Map Visualization

The application uses Leaflet.js to visualize vehicle data on an interactive map. The map displays markers representing each vehicle's location. Each marker includes information about the vehicle, such as its ID and speed.

# CSV Data Folder

The CSV data folder (csv) is used to store the CSV files that contain vehicle data for uploading. After data is successfully uploaded, the CSV file is moved to the processed folder.
