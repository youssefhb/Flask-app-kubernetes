#!/bin/bash

echo installing dependencies ..

sudo pip2.7 install --upgrade pip
sudo pip2 install -r requirements.txt

echo Installation done !



# If using OpenSuse
sudo zypper in docker-compose

# Uses the Dockerfile to build a new image and starts the container
docker-compose -f docker-compose-build.yml up  -d


# Creates and starts the container
docker-compose  up  -d
# or
docker-compose -f docker-compose.yml up  -d