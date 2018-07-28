# Homeless Entrepreneur
We will end homelessness together. Using this free, Open Source application, any city government/VSO/NGO can launch the program and develop opportunities. Main purpose of backend is to provide easy to use dahsboard and enrollment services. The backend currently serves all views in Microservices APIs. Used by Homeless Entrepreneur Android Application (Hosted here: Homeless Entrepreneur [Android])

## Pre-Requisites:
Homeless Entrepreneur Backend uses Python version 2.7, PIP and PGSQL as datastore. Make sure you have these installed. 

## Installation Notes:

### Create Virtual Environment
Setup your new virtual environment and do following steps.

### Install Django
Inside Virtual Environment, Install Django
https://docs.djangoproject.com/en/2.0/topics/install/

### Install Dependencies for App:

#### Install GeoDjango
Inside Virtual Environment, Install Django
https://docs.djangoproject.com/en/2.0/ref/contrib/gis/install/

#### Install Django Rest Framework
http://www.django-rest-framework.org/
  pip install djangorestframework

#### Install Djoser
https://github.com/sunscrapers/djoser
  pip install djoser

#### Install Django Simple History
https://django-simple-history.readthedocs.io/en/latest/
  pip install django-simple-history

#### Install psycopg2
Used for Connecting PGSQL Database
  pip install psycopg2

#### Install Django Rest Framework JWT
https://github.com/GetBlimp/django-rest-framework-jwt
  pip install djangorestframework-jwt

## Clone Homeless Entrepreneur App Code
you will need to edit settings.py file in erefugio and add your own temeplate directory.
create PGSQL database with POSTGIS extension 

run 
     python manage.py runserver 
in root directory of app code to run server on the localhost.


# For Contributions: 
We will be soon releasing [Homeless Entrepreneur OSS Guide](#) for information on how to get started contributing to the project.

# License:
We are Apache 2.0 Licensed. 
