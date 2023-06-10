# UNAL EXTENSION

This is a University project made with the Django Framework that tries to representante the National University Extension module. This is the final project of the subject Databases.

## Tech Stack

**Client:** HTML5, CSS3

**Server:** DJANGO

**DB:** MYSQL




## Run Locally

Clone the project

```bash
  git clone https://github.com/FabianEspitia-it/ExtensionUNAL-DJANGO.git
```

Go to the project directory

```bash
  cd my-project
```

Create Virtual Environment

```bash
 Py -m venv venv

```

Active The Virtual Environment

```bash
 .\venv\Scripts\activate
```

Install Django

```bash
  pip install django
```

Go to File that Contains settings.py Program

```bash
  cd my_file
```

Change The DATABASES Constant

```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'databaseName',
        'USER': 'userName',
        'PASSWORD': 'yourPassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Go to File that Contains manage.py Program

```bash
  cd my_file
```
Run server

```bash
  py manage.py runserver
```
