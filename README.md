<!-- Please update value in the {}  -->

<h1 align="center">Django Quiz App</h1>


<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Overview](#overview)
- [Stack & Tools](#stack)
- [Project Structure](#project-structure)
- [How to use](#how-to-use)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

This is a back-end flight-app project made with Django DRF. I have used different third party apps to develop 

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

## Project Structure

```bash
.──── django-quiz-app (repo)
│
├── main
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── quiz
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
├── db.sqlite3
├── django-quiz-app-gif.gif
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

# Add .env file
    add your SECRET_KEY in a .env file

# Run the app
    $ python manage.py runserver
```

## Contact

- [Linkedin](https://www.linkedin.com/in/mustafa-kose-linked/)
- [GitHub](https://github.com/MSKose)