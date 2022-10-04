<!-- Please update value in the {}  -->

<h1 align="center">Django Flight App</h1>


<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Overview](#overview)
- [Stack & Tools](#stack)
- [Notes](#notes)
- [Project Structure](#project-structure)
- [How to use](#how-to-use)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

This is a back-end flight-app project made with Django DRF. I have used different tools to develop this project, including drf-yasg, django toolbar, and django rest auth

<!-- ![screenshot](https://user-images.githubusercontent.com/16707738/92399059-5716eb00-f132-11ea-8b14-bcacdc8ec97b.png) -->
<!-- ![screenshot](./django-quiz-app-gif.gif) -->
<p align="center">
  <img src="./django-quiz-app-gif.gif">
</p>

<h2 id="stack">Stack & Tools</h2>

- Django
- Django Rest Framework
- drf-yasg (Swagger generator)
- Django Debug Toolbar
- dj-rest-auth

## Notes
## Installing Swagger

- Swagger is an open source project launched by a startup in 2010. The goal is to implement a framework that will allow developers to document and design APIs, while maintaining synchronization with the code.
- Developing an API requires orderly and understandable documentation.
- To document and design APIs with Django rest framework we will use `drf-yasg` which generate real Swagger/Open-API 2.0 specifications from a Django Rest Framework API.
- You can find the documentation [here](https://drf-yasg.readthedocs.io/en/stable/readme.html). Install drf-yasg with the code below;

```python
pip install drf-yasg
```

- In the settings.py add the following;

```python
# settings.py
INSTALLED_APPS = [ 
   ... 
   'django.contrib.staticfiles', # Required for serving swagger ui's css/js files. You might have this line already 
 
   # Third party apps: 
   'drf_yasg', 
   ... 
]
```

- Here is the updated urls.py for swagger. In swagger documentation, those patterns are not up-to-date. Modify urls.py like this instead;

```python
# urls.py
from django.contrib import admin
from django.urls import path
# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Flight Reservation API",
        default_version="v1",
        description="Flight Reservation API project provides flight and reservation info",
        terms_of_service="#",
        contact=openapi.Contact(email="test@test.com"),  # Change e-mail on this line!
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("admin/", admin.site.urls),
    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schemaredoc"),
]
```

- And finally, migrate;

```python
python manage.py migrate
```

- You can now see the pages `{base-url}/swagger/` or `{base-url}/redoc/`

## Installing Django Debug Toolbar
- The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel’s content.
- See the Django Debug Toolbar [documentation page](https://django-debug-toolbar.readthedocs.io/en/latest/).
- Installing it on your machine;

```python
pip install django-debug-toolbar
```

- Add the following to your urls.py;

```python
# urls.py
from django.urls import include
urlpatterns = [
    ...
    path('__debug__/', include('debug_toolbar.urls')),
]
```

- Add this middleware to the top of your MIDDLEWARE list;

```python
# settings.py
MIDDLEWARE = [
    # debug-toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    # default middlewares;
    ...
]
```

- And finally add the following configuration of internal IPs to your settings.py;

```python
# settings.py
INTERNAL_IPS = [
    "127.0.0.1",
]
```

## Project Structure

```bash
.──── django-flight-app (repo)
│
├── README.md
├── db.sqlite3
├── main
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## How To Use 

To clone and run this application, you'll need [Git](https://git-scm.com)

```bash
# Clone this repository
$ git clone https://github.com/MSKose/django-flight-app

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt

# Add the following to your .env file
    SECRET_KEY=<yourSecretKeyHere>
    DEBUG=True # switch to True when in production
    ENV_NAME=dev # switch to prod when in production
    DEBUG=True 
    SQL_DATABASE=<yourDatabaseProjectName>
    SQL_USER=<yourDatabaseUsername> 
    SQL_PASSWORD=<yourDatabasePassword>
    SQL_HOST=localhost 
    SQL_PORT=5432

# Run the app
    $ python manage.py runserver
```

## Contact

- [Linkedin](https://www.linkedin.com/in/mustafa-kose-linked/)
- [GitHub](https://github.com/MSKose)