# apiPrepiChallenge
API developed in Django + DRF for Prepi Challenge.

# Project Setup step-by-step:
## 1. Initializing the virtual enviroment in project directory:
  Run commands (Windows OS):
```
  python -m venv env
  env\Scripts\activate
  python -m pip install --upgrade pip
  pip install django
  pip freeze > requirements.txt
  pip install -r requirements.txt
```
## 2. It's necessary the instalation of libraries found in requirements.txt. To install them, run:
```
  pip install libraryName
```
## 3. With terminal open and virtual env activated, run:
```
  python manage.py makemigrations
  python manage.py migrate
```
## 4. You will need to create a super user to front integration:
```
  python manage.py createsuperuser
```
## 5. Now, run the server:
```
  python manage.py runserver
```
## 6. Access the localhost:8000/admin page on web and login with super user infos.
## 7. Go to 'Tokens' section, and copy the super user's token.
## 8. Now you can proceed to Front-end Setup.
