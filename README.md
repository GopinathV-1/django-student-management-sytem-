# Django Toy Project

A simple CRUD project using the django framework

This repo consists of a source code of a python script and SQLAlchemy to make an interactive student management system
using **Django** framework

## How is it done?

You might be wondering that how the application performs many operations like creation, deletion, and update of assignments. Well, it was not that complicated as you may think. All these were achieved with the help of Database operation. 

We all know that computers can store and retrieve data easily, so in order to do this operation, we used the Database. We have used queries to pick and formulate the data in a specific structure from Database. This repo consists of a basic example of how to do that.


## Getting start

To get started with the code on this repo, you need to either *clone* or *download* this repo into your machine just as shown below;

```bash
git clone git@gitlab.com:mountblue/cohort-16-python/gopinath_v/django-toy-project.git
```

## Running the App

### Part 1: Create Database and virtualenv

### Create Database
```bash
$ sudo -u postgres psql
```

```bash
postgres=# \i create_db.sql
```

```bash
postgres=# \q
```

### Install the virtualenv package
```bash
$ pip install virtualenv
```
### Create the virtual environment
To create a virtual environment, you must specify a path. You may provide any name in the place of <mypython>:
```bash
$ virtualenv <mypython>
```
  
### Activate the virtual environment
```bash
$ source mypython/bin/activate
```

Now you can load the requirements.txt.
## Dependencies

Before running the application, you need to have some packages preinstalled. So I have provided all the required packages and their versions in requirements.txt file by running the below command you will be able to install all the packages.

```bash
$ pip install -r requirements.txt
```

#### Part 1: Create and provide information to .env file.

To run this, you need to create and provide the environment values in .env file.

### Move to project directory
```bash
$ cd django-toy-project
```

### Create .env file
create a .env file **inside studentapp folder**

```bash
$ cd studentapp
$ touch .env
```
#### provide these information inside .env file.

```bash
EMAIL_USER=YOUR_EMAIL_ID
EMAIL_PASSWORD=YOUR_PASSWORD
SECURITY_KEY=GENERATED_ONE
```
##### NOTE: Do not provide space inbetween = and key,value inside .env file

#### open the terminal

#### SECRET_KEY generation

```bash
$ python3
>>> import secrets
>>> secrets.token_hex(16)
```
Provide **email id and password** in .env file. 

#### for creating and accessing admin operations create superuser

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
##### Note: provide your username and password in required place to create admin user.

#### Part 3: Running the application on server

```bash
$ python3 manage.py runserver

```
Now you can access the app on your local server

### Deactivate the virtual environment
if you have followed step1, use this command to get out of virtualenv
```bash
$ deactivate

```
### Delete Database
```bash
$ sudo -u postgres psql
```

```bash
postgres=# \i delete_db.sql
```

```bash
postgres=# \q
```
