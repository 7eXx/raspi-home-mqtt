# MQTT Mosquitto
This project aims to create a middleware with mqtt using mosquito.  
A client periodically publish some informations in a topic.
A secondary client listens for eventually new update in the previous topic.

## Publisher
It a python project stored in ***publisher*** folder:  

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

Execute the following command to start the publisher:
```
$ python src/publisher/main.py
```

# Subscriber:
It a javascript project stored in ***subscriber*** folder:  

Install all dependencies with:
```
$ npm install
```
Run the project with:
```
$ npm run dev
```