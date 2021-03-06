# GSheetsAPI
API developed in Django + DRF and linking informations to a Google Sheets.

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

# Some util informations:
- This project is connected with the Google Sheets API by the 'gspread' library (https://pypi.org/project/gspread/);
- All functions and code related to Google Sheets API can be found in spreadsheet.py;
- To get connected with the Google Sheet that the server is connected, click in the link: https://docs.google.com/spreadsheets/d/1w-mgy_DsnAaw6lFnV9xmeDfzQy2_iWIzUYjLUhX6SxA/edit?usp=sharing


