# AppsAPI

Test task. Simple API. 

The API allows you to create, read, update, and delete data in the Apps model. 

“Apps” is a model that stores external sources that have access to the API.

 The Apps model has the following fields: id, title, description, api_key, created_date. 
 Using API you can set the only title, description fields, new api_key, id and current data will be generated automatically.

## How to install

#### Requirements (see Pipfile for details):
- python 3.6
- django 2.2
- djangorestframework
- djangorestframework-api-key

Create a virtual environment and install dependencies with [pipenv](https://github.com/pypa/pipenv):
```sh
pipenv install
pipenv shell
```
Apply migrations and create a user:
```sh
cd apps_api_project
python manage.py migrate
```
There are two ways to create your first API key:
1. Create user
    ```
    python manage.py createsuperuser
    ```
    and use django admin to add new API key
2. Or you can add API key in django shell:
    ```
    python manage.py shell
    >>> from rest_framework_api_key.models import APIKey
    >>> api_key, key = APIKey.objects.create_key(name="my_first_api_key")
    >>> key
    'aby3suNl.SZ2iq5vPdI441VOjhz23CqCVbYqKXg0n'
    ``` 
#### Run the server:
```sh
python manage.py runserver 
```

### How to use the API
Clients must pass their API key via the Authorization header. It must be formatted as follows:
`Authorization: Api-Key ********`
where `********` refers to the generated API key.

`http://127.0.0.1:8000/api/` - list of the apps

`http://127.0.0.1:8000/api/app_name` - data of the 'app_name' app

You can use different HTTP clients for working with API, for instance, it can be `curl`, [HTTPie](https://httpie.org/) or [Postman](https://www.postman.com/).
I've provided the examples with HTTPie.
#### Get list of all apps
```
http  http://127.0.0.1:8000/api/ 'Authorization: Api-Key ********'
```
#### Create new app
```
http POST  http://127.0.0.1:8000/api/ 'Authorization: Api-Key ********' title=new_app description='new app description'
```
#### Read details of the app
```
http  http://127.0.0.1:8000/api/new_app 'Authorization: Api-Key ********'
```

#### Update the app
```
http PUT  http://127.0.0.1:8000/api/new_app 'Authorization: Api-Key ********' title='new_app' description='updated app description
```

#### Delete the app
```
http DELETE http://127.0.0.1:8000/api/new_app 'Authorization: Api-Key ********'
```
