# INFORCE PYTHON TASK
##ACTUAL TASK:
A company needs internal service for its 'employees which helps them to
make a decision at the lunch place. Each restaurant will be uploading menus
using the system every day over API.
Employees will vote for the menu before leaving for lunch on a mobile app
for whom the backend has to be implemented. There are users who did not
update the app to the latest version and the backend has to support both
versions. The mobile app always sends the build version in headers
##API FUNCTIONALITY:
- Authentication
- Creating restaurant
- Uploading menu for restaurant (There should be a menu for each day)
- Creating employee
- Getting current day menu
- Getting results for the current day
##REQUIREMENTS:
- Only Back End (no needs to add UI);
- REST architecture;
- Tech stack: Django + DRF, JWT, PostgreSQL, Docker(docker-compose);
- README.md with a description of how to run the system;

## Setup
Make containers and run
```bash
docker-compose up -d --build
```
Run containers
```bash
docker-compose up
```
Stop containers
```bash
docker-compose down
```
Scrip to create super user or make migrations or migrate
```bash
docker-compose exec web python manage.py createsuperuser
```
 
### After that, add in Django administration two user groups - "user"  and  "restaurant" 

# Main APIs
API to register for user. \
POST - username, password.
```bash
http://127.0.0.1:8000/api/registration/user/
```
\
API to register for restaurant. \
POST - username, password.
```bash
http://127.0.0.1:8000/api/registration/restaurant/
```
\
API to take JWT, take access token and use it with `Bearer` to have access to GET and POST API. \
POST - username and password and return JWT.
```bash
http://127.0.0.1:8000/api/token/
```
\
API to get all menus for today. \
(access only for users)
```bash
http://127.0.0.1:8000/api/v1/list/
```
\
API to post the menu for any day. \
POST - text field menu and date (default - today). \
(access only for restaurant)
```bash
http://127.0.0.1:8000/api/v1/create/
```
\
API to post user choice for today. User can choose only once a day.\
POST - restaurant name.  \
(access only for users)
```bash
http://127.0.0.1:8000/api/v1/voting/
```
\
API to get info who voted for whom for today. \
(access only for admin)
```bash
http://127.0.0.1:8000/api/v1/voting/admin/
```
\
API to get result of voting, return which restaurant and how many votes. \
(access only for admin)
```bash
http://127.0.0.1:8000/api/v1/result/
```

## PyTest
```bash
docker-compose exec web pytest
```

