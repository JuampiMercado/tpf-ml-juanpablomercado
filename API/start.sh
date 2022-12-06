#!/bin/sh
echo "Starting application..."
if [[ "$(docker images -q apiimage:latest 2> /dev/null)" == "" ]]; then
    echo "Creating docker image..."
  docker build -t apiimage .
else
    echo "Image already exists..."
fi
echo "Starting docker container..."
docker run -it -d --name mlapicontainer -p 80:80 apiimage
