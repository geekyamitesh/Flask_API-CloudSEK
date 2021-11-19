# Flask API
This project is created by [GeekyAmitesh](https://www.github.com/geekyamitesh) 


### Dependencies

* [Python](https://www.python.org/) - Programming Language
* [Flask](https://flask.palletsprojects.com/) - The framework used
* [SQLAlchemy](https://docs.sqlalchemy.org/) - ORM
* [Pip](https://pypi.org/project/pip/) - Dependency Management
* [Representational State Transfer](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) - Article by Roy Fielding

### Virtual environments

```
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask

```

Install all project dependencies using:

```
$ pip install -r requirements.txt
```

### Running
 
```
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ python -m flask run
```


```
flask run --host=0.0.0.0
```


### SQLAlchemy

Step 1 - Install the Flask-SQLAlchemy extension.

```
pip install flask-sqlalchemy

```
Step 2 - You need to import the SQLAlchemy class from this module.

```
from flask_sqlalchemy import SQLAlchemy

```
Step 3 - Now create a Flask application object and set the URI for the database to use.

```
app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```


### Docker 

```
sudo docker build --tag amitesh_docker_api 
sudo docker run amitesh_dcoker_api

```


## Contributing

This API was developed based on:

[Flask documentation](https://flask.palletsprojects.com/)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



## Facing Any Problem or need any Help:grey_question:
Write me in [issues](https://github.com/geekyamitesh/voiceAi-based-webapp/issues) section. I will try solve your issue within 10-12 hours.
</br>***Keep Developing and Destroying.*** :wink:

<p align="center">
  <i>Take a look at my repositories and let's get in touch!</i>

<p align="center">
<a href= "https://github.com/geekyamitesh"><img src="https://img.icons8.com/material-outlined/27/000000/ball-point-pen.png"/></a>
<a href= "https://www.linkedin.com/in/geekyamitesh/"><img src="https://img.icons8.com/material-outlined/30/000000/linkedin.png"/></a>
<a href= "https://twitter.com/geekyamitesh"><img src="https://img.icons8.com/material-outlined/30/000000/twitter.png"/></a>
<a href= "https://geekyamitesh.github.io/amitesh/"><img src="https://img.icons8.com/material-outlined/27/000000/geography.png"/></a>
</p>

</p>

