<img align="right" width="33%" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png">

<img  width="15%" src = "https://user-images.githubusercontent.com/92718918/225281321-22416455-e553-4981-a355-b59d2750331c.jpg">

<h1 align="center">Mongodb to Mongodb <br> Data transfer</h1>
 
## About
To convert data from one MongoDB database to another using Python, we can use the PyMongo library.


## Use Cases

 here are a few use cases where you may want to convert data from one MongoDB instance to another MongoDB Instance using Python:
- from Server to Local Mongo db
- from Local to Server Mongo Db
- from Server to Server Mongo Db

In all of these use cases, Python and the pymongo library provide a powerful and flexible way to manipulate MongoDB data and transfer it between instances.


## Summary
 some times we have the data in server, but not in the local <br />in that 
 time it is very useful to take the data from <br /> server 
 database into local database <br /> here we use the languages are python,django,html


## Requirements 
- pip install pymongo
- pip install django
- pip install djongo


## Running Mongodb 2 mongodb
To run this, you have to follow the below steps
- first, clone the repositry
- Ensure you are in mongo2mongo folder, if not please change directory to mongo2mongo folder
- Then run this command in terminal `python manage.py runserver`
- click on the local host (http://127.0.0.1:8000/)

## For developers
developers can modify the file (views.py)

## Steps to Access the Application 

1. Clone the Repository 
2. python manage.py runserver  
3. Open the application on local host (http://127.0.0.1:8000/) and add below mentioned URL parameters for the functionality required.

   3.1. for Server to Local enter "/servertolocal" 
  
   3.2. for local to server enter "/localtoserver"
 
   3.3. for server to server enter "/servertoserver"

![image](https://user-images.githubusercontent.com/92718918/228515756-bbdcfaae-ce7d-4750-bf08-af331f28da88.png)

- Server to Local (best use for taking manual backup)
![image](https://user-images.githubusercontent.com/92718918/228516516-41be4ee9-b14d-4aac-a7ed-ed3844d988c9.png)

- Local to Server (best use for updating / or deploying new db to server)
![image](https://user-images.githubusercontent.com/92718918/228517006-b9f6b6ec-323b-4f8f-a756-608fd2850bbc.png)

- Server to Server (best use for migrating database to another instance)
![image](https://user-images.githubusercontent.com/92718918/228518422-3c521d5a-c1fd-46d8-8ffa-f4d914adf90a.png)



<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
 </p>
