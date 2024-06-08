# Django Conversation Summary Project

## Project Setup and Configuration

### 1. Install Python and Django

Ensure Python is installed. Download from [python.org](https://www.python.org/).

Install Django using pip:

```sh
pip install django


Create a Django Project
Start a new Django project:
django-admin startproject myproject
cd myproject

Create a Django App
Start a new app within your project:
python manage.py startapp myapp


Configure the App
Add myapp to INSTALLED_APPS in myproject/settings.py:
INSTALLED_APPS = [
    # ... other installed apps ...
    'myapp',
]


Run Initial Migrations
Apply initial database migrations:
python manage.py migrate


Run the Development Server
Start the development server:
python manage.py runserver


