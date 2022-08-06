# MQTT Mosquitto
This project aims to create a middleware with mqtt using mosquito.  
A client periodically publish some informations in a topic.
A secondary client listens for eventually new update in the previous topic.

## Middleware
It is made by a Docker file which uses an mqtt-mosquitto middleware based on Debian.
To run it, just use the docker-compose file:
```
$ docker-compose up -d
```

## Backend
It a python project stored in ***backend*** folder, so move in to this directory.

Using the following command to create a virtual environment in python:
```
$ virtualenv venv
```
Activate the virtual environment:
```
$ ./venv/bin/activate
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
