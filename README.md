# test_tle_tracker
follow the ISS
# TO INSTALL:
conda create --name isspython python=3.11 flask

# TO RUN FLASK SERVER + QUERY LOCATION
python -m flask --app app run -> start flask server
python globe.py -> Poll for realtime status on ISS
