#!/bin/bash

sudo apt install python3-pip


mkdir  EjPractico2
cd EjPractico2

mkdir .venv
touch app.py
mkdir static
cd static
mkdir css
mkdir images
cd ..

mkdir templates

pipenv install flask
pipenv shell

export FLASK_APP=app.py
export FLASK_DEBUG=1

flask run
