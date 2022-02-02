# MQTT Mosquitto
This project aims to create a middleware with mqtt using mosquito.  
A client periodically publish some informations in a topic.
A secondary client listens for eventually new update in the previous topic.

## 
Create a virtual environment in python
```
$ virtualenv venv
```
Activate the virtual environment
```
$ ./venv/bin/activate
```
Install all dependencies

```
$ pip install -r requirements.txt
```

## Run publisher
Execute the following command:
```
$ python src/publisher/main.py
```