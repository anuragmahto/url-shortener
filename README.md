# infracloud-assignment

## Project Name
tinyurl

## App Name
urlapp

## Description
TinyURL is a Django-based web application that provides URL shortening services. Users can input a long URL and get a shortened version that redirects to the original URL when user click on the short url. It is designed to be simple, efficient, and user-friendly.

---

## Features
- Generate shortened URLs from long URLs.
- Redirect shortened URLs to their original destination.
- Display top 3 domain names that have been shortened the most of the times.

---

## Technology Stack
- **Backend**: Django (Latest Version)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default)

---

## Setup and Installation

### Prerequisites
1. Python 3.12
2. Django 5.1.4
4. Virtual Environment Tool (venv, virtualenv)

---

### Environment Setup
1. Clone the repository:
   ```
   git clone https://github.com/anuragmahto/infracloud-assignment
   cd tinyurl
   ```

2. Create a virtual environment:
   ```
   python3 -m venv infra_env
   ```

3. Activate the virtual environment:
   ```
     source infra_env/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python3 manage.py migrated
   ```

7. Run the application:
   ```
   python3 manage.py runserver
   ```

---

## Usage
1. Access the application at `http://127.0.0.1:8000/`.
2. Enter a long URL in the input field and generate a shortened URL.
3. Use the shortened URL to get redirected to the original URL.

---
## Project Structure
```
tinyurl/
|-- urlapp/
|   |-- migrations/
|   |-- static/
|   |-- templates/
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- tinyurl/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- manage.py
|-- requirements.txt
|-- db.sqlite3
|-- infra_env
```