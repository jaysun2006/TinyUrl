### TinyUrl: (UrlShortner) Service



## Solution:

### Setup:

## Make Python 3 Virtual Environment

    virtualenv -p python3 toolenv


## Activate Virtualenv

     * source toolenv/bin/activate



## Now Go to Main Repo:

     * cd <repo folder>

## Install all the python dependency

     pip install -r requirement.txt



## Make Python Migrations

     ● python manage.py makemigrations



## Make Migrations

    python manage.py migrate


## Now Run The backend Server

    python manage.py runserver



### Backend Architectue


1. URL : It keeps all the Url Mapped with tiny slug



## API Structure

    * "Create Tiny url": "http://127.0.0.1:8000/api/",
    * "Redirect url": "http://127.0.0.1:8000/<slug>/",

## API View Strucutre:
    ● Viewset.py : It keeps all the api viewset
    ● serializer.py : It keeps all the Input Data/Output Data formats
    ● permissons.py: It contains all the permission regarding the api endpoint

