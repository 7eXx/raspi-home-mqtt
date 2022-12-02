# MQTT Mosquitto
This project aims to create a middleware with mqtt using mosquito.  
A client periodically publish some informations in a topic.
A secondary client listens for eventually new update in the previous topic.


## Middleware message broker
It is made by a Docker file which uses an mqtt-mosquitto middleware based on Debian.
To run it, just use the docker-compose file:
```
$ docker run --rm -d \
    -v "$(pwd)"/docker/mosquitto/config:/mosquitto/config \
    -v "$(pwd)"/docker/mosquitto/log:/mosquitto/log \
    -v "$(pwd)"/docker/mosquitto/data:/mosquitto/data \
    -p 1883:1883 \
    -p 9001:9001 \
    --name mosquitto \
    eclipse-mosquitto
```

## Backend
It a python project stored in ***backend*** folder, so move in to this directory.

Using the following command to create a virtual environment in python:
```
$ python3 -m venv venv
```
Activate the virtual environment:
```
$ source venv/bin/activate
```
Install all dependencies:

```
$ pip install -r requirements.txt
```
Before execute the main script, it's better to mock the gpio otherwise execution will fail.
```
export GPIOZERO_PIN_FACTORY=mock
```

Execute the following command to start the backend:
```
$ python main.py
```

### Build push docker image
use the following command to build and push the backend docker image to private registry:
```
$ ./build-push.sh
```

## Client test:
It a javascript project stored in ***client*** folder:  

Install all dependencies with:
```
$ npm install
```
Run the project with:
```
$ npm run dev
```

## Fullstack Configuration
A full configuration is available using the docker-compose file from the root directory:
```
$ docker-compose up -d
```
This will use the backend pushed image, and the mosquito middleware.