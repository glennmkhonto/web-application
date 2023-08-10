# web-application

The Vehicle Tracking Web Application is a Flask-based web application that allows users to manage and visualize vehicle data using an interactive map. This README provides information on the app's design, database model, and instructions for launching the app.

# Application Design

The application follows a client-server architecture with the following key components:

*Frontend: The frontend is built using HTML, Bootstrap for styling, and Jinja2 templating for dynamic rendering of data.

*Backend: The backend is implemented using Flask, a Python web framework. It handles routes, database interactions, and rendering templates.

*Database: The app uses a Postgresql database to store vehicle data. The SQLAlchemy ORM is employed to interact with the database.

*Map Visualization: The Leaflet.js library is used for interactive map visualization, with vehicle markers representing location data.

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


##### Be sure to enter your db password in docker-compose, Dockerfile and app.py  

# Makefile

Use the make file to easily use commands to run

# Database Configuration

The application now uses a PostgreSQL database to store vehicle data. Here's how you can configure the database:

1. **Install PostgreSQL:**

   Make sure you have PostgreSQL installed on your system. You can download and install it from the [PostgreSQL official website](https://www.postgresql.org/download/).

2. **Configure Database Connection:**

Run the following commands to apply the necessary migrations and create the required tables in your PostgreSQL database:
* flask db init
* flask db migrate -m "Initial migration"
* flask db upgrade


3. **Configure Database Connection:**

   Open the `app.py` file and locate the `app.config` section. Update the `SQLALCHEMY_DATABASE_URI` to connect to your PostgreSQL database:

   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost/webappdb'


# Launching the Application

Follow these steps to launch the Vehicle Tracking Web App:

1) Clone the Repository:

*git clone https://github.com/glennmkhonto/web-application.git
*cd web-application

2) Install Dependencies:

pip install -r requirements.txt

3) Configure Database:

*Open app.py and update the SQLALCHEMY_DATABASE_URI in the app.config section to your database connection string.

4) CSV Data Upload:

*Place your CSV file in the csv folder at the root of the project directory.

*Run the Flask app to upload data from the CSV file into the database:

*ython app.py

*The CSV file will be moved to the processed folder after processing.

Run the App:

*python app.py

Access the App:

*Open your web browser and navigate to http://localhost:5000.
*You can manage and visualize vehicle data using the provided web interface.

## Running the Application with Docker Compose

To test the application using Docker Compose, follow these steps:

1. Install Docker and Docker Compose on your system if you haven't already.
4. Build the Docker images and start the containers: `docker-compose up --build`

Once the containers are up and running, you can access the application by opening your web browser and navigating to http://localhost:5000.

To stop the containers, press `Ctrl+C` in the terminal where you started Docker Compose. To remove the containers and associated resources, run `docker-compose down`.

Note: You may need to adjust the configuration in the docker-compose.yml file to match your environment and application setup.


# Funtionality

    View Map:
    *To view the vehicle data on a map, click on the "View Map" link in the navigation menu.

    Manage Vehicle Data:
    *You can manage vehicle data by adding, updating, and deleting records.
    *To add a new vehicle, click the "Add New Vehicle" button and fill in the details.
    *To update a vehicle's information, click the "Edit" button next to the respective record.
    *To delete a vehicle's record, click the "DELETE" button next to the respective record. A confirmation dialog will appear, then click "ok" if happy to proceed.

# Map Visualization

The application uses Leaflet.js to visualize vehicle data on an interactive map. The map displays markers representing each vehicle's location. Each marker includes information about the vehicle, such as its ID and speed.

# CSV Data Folder

The CSV data folder (csv) is used to store the CSV files that contain vehicle data for uploading. After data is successfully uploaded, the CSV file is moved to the processed folder.

