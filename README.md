# Excer Force Gym


## Overview:
This is a gym servise website. this simple website allows an authorized client to view the training classes and coaches information that is saved in the database. It also allows an authorized manager to view, add and delete training classes and coaches information and also allows them to update a class information.
this website uses Auth0 as a authentication provider and herokuapp for hosting deployment.

## Motivation:
Excer Force is the name of the gym I workout at and it has no offical website or app so the reservations 
,viewing of the classes and other managment tasks are done by communicating with the managment by whatsapp which is not convenient for the clients or the managment. What motivated me to do this project is that maybe I could scale it and finish all the required tasks and give it to them.


## Getting Started:
clone the repastory to run localy
https://github.com/SuaadAiman/excer-force-gym-project.git

### Initialize and activate a virtualenv using:
for mac and linux:
''''

python -m virtualenv env
source env/bin/activate

''''

for windows:
''''

python -m virtualenv env
source env/Scripts/activate

''''

### Install the dependencies:
''''
pip install -r requirements.txt

''''

### create database localy (only if )
dropdb gym_test
createdb gym_test
dropdb capstone
createdb capstone

### Run the development server:
''''
source setup.sh
FLASK_APP=app.py FLASK_DEBUG=true flask run

''''


## Testing the project
The project does not have a frontend but can be tested by these commands below and also
by the running the test_app.py file

### 1. Add a coach:

''''
curl --request POST \
  --url https://excer-force-gym.herokuapp.com/Coaches \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGQxOTZmZjg2ZjYwMDZhMzU1MWViIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNjY4MDYzLCJleHAiOjE2MzM3NTQ0NjMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Q29hY2hlcyIsImRlbGV0ZTpUcmFpbmluZ0NsYXNzZXMiLCJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiLCJwYXRjaDpUcmFpbmluZ0NsYXNzZXMiLCJwb3N0OkNvYWNoZXMiLCJwb3N0OlRyYWluaW5nQ2xhc3NlcyJdfQ.nM-_z-GUfR72FuO5ysgIi5QtyqrU3kHFsVe6n754zson04VErfnq9-SQDi1jTRZ19mvop2CXIN6GW-7vbxpIYj7jHCzX8E2x2oJcY13sRhgJ74fmHUJXMW2fbiwpd1-VS-3zo_4nukRBm8O5bwy_sD-8g218m0kXxoQGC3IHzymmywQX9gNcuabWuMjNEq-wLE8MjtHoIYKQyMKwE_u0c-fUUC-GOuA9ibaMFMMvZjuL9xZNLEQ2bzB3SGGKsgb7S674aIzbyAtbt3-LQA8Gphw_LCdIHl1FBnVbYaKDghJbcEpMkL2g_5UHmlId8frqUBCl6z_zouScrenlH0xsNA' \
  --header 'Content-Type: application/json' \
  --data '{"name":"Hanaa","description":"body building and cardio trainer"}'

''''

### 2. Get coaches:

''''
curl --request GET \
  --url https://excer-force-gym.herokuapp.com/Coaches \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGQxOTZmZjg2ZjYwMDZhMzU1MWViIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNjY4MDYzLCJleHAiOjE2MzM3NTQ0NjMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Q29hY2hlcyIsImRlbGV0ZTpUcmFpbmluZ0NsYXNzZXMiLCJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiLCJwYXRjaDpUcmFpbmluZ0NsYXNzZXMiLCJwb3N0OkNvYWNoZXMiLCJwb3N0OlRyYWluaW5nQ2xhc3NlcyJdfQ.nM-_z-GUfR72FuO5ysgIi5QtyqrU3kHFsVe6n754zson04VErfnq9-SQDi1jTRZ19mvop2CXIN6GW-7vbxpIYj7jHCzX8E2x2oJcY13sRhgJ74fmHUJXMW2fbiwpd1-VS-3zo_4nukRBm8O5bwy_sD-8g218m0kXxoQGC3IHzymmywQX9gNcuabWuMjNEq-wLE8MjtHoIYKQyMKwE_u0c-fUUC-GOuA9ibaMFMMvZjuL9xZNLEQ2bzB3SGGKsgb7S674aIzbyAtbt3-LQA8Gphw_LCdIHl1FBnVbYaKDghJbcEpMkL2g_5UHmlId8frqUBCl6z_zouScrenlH0xsNA' 

''''
### 3. delete coach:

''''
curl --request DELETE \
  --url https://excer-force-gym.herokuapp.com/Coaches/4 \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGQxOTZmZjg2ZjYwMDZhMzU1MWViIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNjY4MDYzLCJleHAiOjE2MzM3NTQ0NjMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Q29hY2hlcyIsImRlbGV0ZTpUcmFpbmluZ0NsYXNzZXMiLCJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiLCJwYXRjaDpUcmFpbmluZ0NsYXNzZXMiLCJwb3N0OkNvYWNoZXMiLCJwb3N0OlRyYWluaW5nQ2xhc3NlcyJdfQ.nM-_z-GUfR72FuO5ysgIi5QtyqrU3kHFsVe6n754zson04VErfnq9-SQDi1jTRZ19mvop2CXIN6GW-7vbxpIYj7jHCzX8E2x2oJcY13sRhgJ74fmHUJXMW2fbiwpd1-VS-3zo_4nukRBm8O5bwy_sD-8g218m0kXxoQGC3IHzymmywQX9gNcuabWuMjNEq-wLE8MjtHoIYKQyMKwE_u0c-fUUC-GOuA9ibaMFMMvZjuL9xZNLEQ2bzB3SGGKsgb7S674aIzbyAtbt3-LQA8Gphw_LCdIHl1FBnVbYaKDghJbcEpMkL2g_5UHmlId8frqUBCl6z_zouScrenlH0xsNA'

''''

### 4. add a training class:

''''

curl --request POST \
  --url https://excer-force-gym.herokuapp.com/TrainingClasses \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGQxOTZmZjg2ZjYwMDZhMzU1MWViIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNjY4MDYzLCJleHAiOjE2MzM3NTQ0NjMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Q29hY2hlcyIsImRlbGV0ZTpUcmFpbmluZ0NsYXNzZXMiLCJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiLCJwYXRjaDpUcmFpbmluZ0NsYXNzZXMiLCJwb3N0OkNvYWNoZXMiLCJwb3N0OlRyYWluaW5nQ2xhc3NlcyJdfQ.nM-_z-GUfR72FuO5ysgIi5QtyqrU3kHFsVe6n754zson04VErfnq9-SQDi1jTRZ19mvop2CXIN6GW-7vbxpIYj7jHCzX8E2x2oJcY13sRhgJ74fmHUJXMW2fbiwpd1-VS-3zo_4nukRBm8O5bwy_sD-8g218m0kXxoQGC3IHzymmywQX9gNcuabWuMjNEq-wLE8MjtHoIYKQyMKwE_u0c-fUUC-GOuA9ibaMFMMvZjuL9xZNLEQ2bzB3SGGKsgb7S674aIzbyAtbt3-LQA8Gphw_LCdIHl1FBnVbYaKDghJbcEpMkL2g_5UHmlId8frqUBCl6z_zouScrenlH0xsNA' \
  --header 'Content-Type: application/json' \
  --data '{"name":"Cardio","description":"Cardio class","coachId":1 , "periods":["1","7"] , "dayes":["sun","wed"]}'

''''
### 5. Get training classes:

''''

curl --request GET \
  --url https://excer-force-gym.herokuapp.com/TrainingClasses \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGQxOTZmZjg2ZjYwMDZhMzU1MWViIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNjY4MDYzLCJleHAiOjE2MzM3NTQ0NjMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Q29hY2hlcyIsImRlbGV0ZTpUcmFpbmluZ0NsYXNzZXMiLCJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiLCJwYXRjaDpUcmFpbmluZ0NsYXNzZXMiLCJwb3N0OkNvYWNoZXMiLCJwb3N0OlRyYWluaW5nQ2xhc3NlcyJdfQ.nM-_z-GUfR72FuO5ysgIi5QtyqrU3kHFsVe6n754zson04VErfnq9-SQDi1jTRZ19mvop2CXIN6GW-7vbxpIYj7jHCzX8E2x2oJcY13sRhgJ74fmHUJXMW2fbiwpd1-VS-3zo_4nukRBm8O5bwy_sD-8g218m0kXxoQGC3IHzymmywQX9gNcuabWuMjNEq-wLE8MjtHoIYKQyMKwE_u0c-fUUC-GOuA9ibaMFMMvZjuL9xZNLEQ2bzB3SGGKsgb7S674aIzbyAtbt3-LQA8Gphw_LCdIHl1FBnVbYaKDghJbcEpMkL2g_5UHmlId8frqUBCl6z_zouScrenlH0xsNA'

'''''

### 6. delete a training class:

''''

curl --request DELETE \
  --url https://excer-force-gym.herokuapp.com/TrainingClasses/4 \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGQxOTZmZjg2ZjYwMDZhMzU1MWViIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNjY4MDYzLCJleHAiOjE2MzM3NTQ0NjMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Q29hY2hlcyIsImRlbGV0ZTpUcmFpbmluZ0NsYXNzZXMiLCJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiLCJwYXRjaDpUcmFpbmluZ0NsYXNzZXMiLCJwb3N0OkNvYWNoZXMiLCJwb3N0OlRyYWluaW5nQ2xhc3NlcyJdfQ.nM-_z-GUfR72FuO5ysgIi5QtyqrU3kHFsVe6n754zson04VErfnq9-SQDi1jTRZ19mvop2CXIN6GW-7vbxpIYj7jHCzX8E2x2oJcY13sRhgJ74fmHUJXMW2fbiwpd1-VS-3zo_4nukRBm8O5bwy_sD-8g218m0kXxoQGC3IHzymmywQX9gNcuabWuMjNEq-wLE8MjtHoIYKQyMKwE_u0c-fUUC-GOuA9ibaMFMMvZjuL9xZNLEQ2bzB3SGGKsgb7S674aIzbyAtbt3-LQA8Gphw_LCdIHl1FBnVbYaKDghJbcEpMkL2g_5UHmlId8frqUBCl6z_zouScrenlH0xsNA'

''''

### 7. patch a training class:

''''

curl --request 'PATCH' \
  --url https://excer-force-gym.herokuapp.com/TrainingClasses/3 \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGQxOTZmZjg2ZjYwMDZhMzU1MWViIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNjY4MDYzLCJleHAiOjE2MzM3NTQ0NjMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Q29hY2hlcyIsImRlbGV0ZTpUcmFpbmluZ0NsYXNzZXMiLCJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiLCJwYXRjaDpUcmFpbmluZ0NsYXNzZXMiLCJwb3N0OkNvYWNoZXMiLCJwb3N0OlRyYWluaW5nQ2xhc3NlcyJdfQ.nM-_z-GUfR72FuO5ysgIi5QtyqrU3kHFsVe6n754zson04VErfnq9-SQDi1jTRZ19mvop2CXIN6GW-7vbxpIYj7jHCzX8E2x2oJcY13sRhgJ74fmHUJXMW2fbiwpd1-VS-3zo_4nukRBm8O5bwy_sD-8g218m0kXxoQGC3IHzymmywQX9gNcuabWuMjNEq-wLE8MjtHoIYKQyMKwE_u0c-fUUC-GOuA9ibaMFMMvZjuL9xZNLEQ2bzB3SGGKsgb7S674aIzbyAtbt3-LQA8Gphw_LCdIHl1FBnVbYaKDghJbcEpMkL2g_5UHmlId8frqUBCl6z_zouScrenlH0xsNA' \
  --header 'Content-Type: application/json' \
  --data '{"periods":["3","7"] , "dayes":["Tue","Thu"]}'

  ''''
### To test the app at once
''''
python test_app.py

''''

## Auth0
The auth0 URL for the project
https://the-gym-project.us.auth0.com/authorize?audience=gym&response_type=token&client_id=3k8MswUFHG3exBdZpb6ayW10MlkVluZy&redirect_uri=https://excer-force-gym.herokuapp.com/

### Users authentication data:
P.s. The access token are stored as variables in the code.

#### 1. Manager:

Email: suaad-an@hotmail.com
Password: 987654321Na
Permissions: The manager can accses all the functions of this project
access_token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGQxOTZmZjg2ZjYwMDZhMzU1MWViIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNjY4MDYzLCJleHAiOjE2MzM3NTQ0NjMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Q29hY2hlcyIsImRlbGV0ZTpUcmFpbmluZ0NsYXNzZXMiLCJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiLCJwYXRjaDpUcmFpbmluZ0NsYXNzZXMiLCJwb3N0OkNvYWNoZXMiLCJwb3N0OlRyYWluaW5nQ2xhc3NlcyJdfQ.nM-_z-GUfR72FuO5ysgIi5QtyqrU3kHFsVe6n754zson04VErfnq9-SQDi1jTRZ19mvop2CXIN6GW-7vbxpIYj7jHCzX8E2x2oJcY13sRhgJ74fmHUJXMW2fbiwpd1-VS-3zo_4nukRBm8O5bwy_sD-8g218m0kXxoQGC3IHzymmywQX9gNcuabWuMjNEq-wLE8MjtHoIYKQyMKwE_u0c-fUUC-GOuA9ibaMFMMvZjuL9xZNLEQ2bzB3SGGKsgb7S674aIzbyAtbt3-LQA8Gphw_LCdIHl1FBnVbYaKDghJbcEpMkL2g_5UHmlId8frqUBCl6z_zouScrenlH0xsNA

#### 2. Client:

Email: suaad_an@hotmail.com
Password: 987654321Na
Permissions: The client can only view the training classes and coaches information
access_token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGRlNTdjNjllYjIwMDcwNGJmY2UzIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNjY4NTkzLCJleHAiOjE2MzM3NTQ5OTMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiXX0.PWvhLyQAEhSlzrtzbklNTkdUZJk-5rvKhEVPP7jgwHRC7U8f9gdRAGJbIgCqyMbPxJkjIhHnpvDq2Ha8QOgm0XSL-BYAvHLa4UshfaFJe0JnR4Quxoa9nexjp-IBzzc5r6RgKLCWpcsx-X504-NoxScu0YrmpVzh0VZA4YcccDBTAmAu_-Hll5OEnNRg7KmmN_7ycHjnBA5JxHWVxOOb0B8xjWIg7xJuJfdWNPkVJnBK3ZgY8VWk2fXFxGJum8NH4t9Lbkp-rwLVytZ0PdGeK47zXXDdoFn9VvFTQPvQHWuJGhNVcpvEj3ajeP5qmhK70QncWToBOY1HIx61vbyh0w


## Endpoints description

### GET '/api/v1.0/TrainingClasses'
- Fetches a dictionary of Training Classes in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: Two objects success and list of trainingClasses object which contains the id, name , description . 
{
  "success": true,
  "trainingClasses": [
    {
      "coachId": 1,
      "dayes": [
        "sat",
        "mon"
      ],
      "description": "body building class",
      "id": 9,
      "name": "body strong",
      "periods": [
        "4",
        "9"
      ]
    },
  ]
}


### POST '/api/v1.0/TrainingClasses'
- Create and a add a new training class to the database using the submitted name, description,associted coach id, periods and dayes of the class.
- Request Body: 
{
    "name":"Cardio",
    "description":"Cardio class",
    "coachId":1 , 
    "periods":["1","7"] ,
    "dayes":["sun","wed"] 
}
- Returns: success value, list of training class with their information and the added class id. 

{
  "added_class": 13,
  "success": true,
  "trainingClasses": [
    {
      "coachId": 1,
      "dayes": [
        "sat",
        "mon"
      ],
      "description": "body building class",
      "id": 9,
      "name": "body strong",
      "periods": [
        "4",
        "9"
      ]
    },]
    
}

#### DELETE '/api/v1.0//TrainingClasses/${class_id}'
- Deletes the training class of the given ID if it exists. 
- Request Arguments: id of the training class - integer
- Returns: A success value, The id of the deleted training class, list of training classes in the database.
{
  "deleted": 13,
  "success": true,
  "trainingClasses": [
    {
      "coachId": 1,
      "dayes": [
        "sat",
        "mon"
      ],
      "description": "body building class",
      "id": 9,
      "name": "body strong",
      "periods": [
        "4",
        "9"
      ]
    },
  ]
}

### PATCH '/api/v1.0//TrainingClasses/${class_id}'
- Update the dayes and periods of a training class giving it's id . 
- Request Body: 
{

    "periods":["1","7"] ,
    "dayes":["sun","wed"] 
}
- Returns: A success value, the id of the updated class and a list of all the class in the database.
{
  "patched": 10,
  "success": true,
  "trainingClasses": [
    {
      "coachId": 1,
      "dayes": [
        "sat",
        "mon"
      ],
      "description": "body building class",
      "id": 9,
      "name": "body strong",
      "periods": [
        "4",
        "9"
      ]
    },
  ]
}

#### GET '/api/v1.0/Coaches'
- View all the coaches information in the database including the name and description. 
- Returns: A success value and list of coaches objects.
{
  "coaches": [
    {
      "description": "body building and cardio trainer",
      "id": 1,
      "name": "Wedyan"
    },
  ],
  "success": true
}

### DELETE '/api/v1.0/Coaches/${coach_id}'
- delete a coach information using the coach id and it also deletes the classes that are associted with the coach. 
- Request Arguments: id of the coach - integer
- Returns: A success value, list of all the coaches plus the deleted coach id.
{
  "coaches": [
    {
      "description": "body building and cardio trainer",
      "id": 1,
      "name": "Wedyan"
    },
  ],
  "deleted": 11,
  "success": true
}
#### POST '/api/v1.0/Coaches'
- Create and a add a new coach to the database using the submitted name and description. 
- Request Body: 
{
    "name":"Wedyan",
    "description":"body building and cardio trainer"
}
- Returns: A success value, the coaches list, the added coach id.
"added_coach": 12,
  "coaches": [
    {
      "description": "body building and cardio trainer",
      "id": 1,
      "name": "Wedyan"
    },
  ],
  "success": true
}

## Deployment 
the website is live on:
https://excer-force-gym.herokuapp.com

## Authors

Suaad Aiman Nabulsi
Email: Suaad-an@hotmail.com

## Acknowledgements
The creation of this website was with the use of conceptes and codes learned in the full-stack nanodegree any code used from outsourses was referenced by a comment near the used code.

















