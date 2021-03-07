# covid-19-app
This is Covid-19 Backend app for getting covid-19 data.

## How to Setup
1. Install python 3.6 or above.
2. Create virtualenv with following command(replace python version as per your system).
```virtualenv covid-app --python=python3.6```
3. Now activate the virtual env and run following command to install the libraries.
```source covid-app/bin/activate```
```pip install -r requirements.txt```
4. Now Create the Database for covid app in mysql using following command.
```create database covid_app```
5. Now replace the username and password of database into env_var.env file like following.
```mysql+pymysql://username:password@localhost/covid_app```
6. Now We need to export the environment variables to the system using following command.
```source env_var.env```
7. Now we need to create the default tables use following command to create it.
```alembic upgrade head```
8. We are done with the pre steps for the setting up the project now run the following 
   command to start the application.
```python app.py```

## Api Details
1. Login API (POST)
http://0.0.0.0:5007/api/v1/login

2. Signup API (POST)
http://0.0.0.0:5007/api/v1/signup

3. Get Covid Data API (POST)
http://0.0.0.0:5007/api/v1/covid

4. Get Covid Report on Mail (GET)
http://0.0.0.0:5007/api/v1/covid/report


## Postman Link for api details
https://www.getpostman.com/collections/5bae1cf1827f59564584
