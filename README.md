This application demonstrates the web framework flask.

chmod u+x install-dependencies.sh   &&   ./install-dependencies.sh
python app-ml.py

# To access the application use the following url.
http://127.0.0.1:5000/




# Using docker, you can build an image called  flask-webapp  tagged latest
docker build -t flask-webapp:latest .


# binds host's port to container port
sudo docker run -d -p 5000:5000 flask-webapp:latest