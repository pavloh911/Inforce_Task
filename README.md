# INFORCE PYTHON TASK

## Setup
```bash
cd app
docker-compose up -d --build
docker-compose exec web python manage.py createsuperuser

```
### After that, add from admin two user groups - "user"  and  "restaurant" 

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

##PyTest
```bash
docker-compose exec web pytest
```

