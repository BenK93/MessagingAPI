# MessagingAPI Django
### API build with django for users to send and receive messages with Token Authentication.
## Users API
--- 
#### Ragistering a new user:
> curl -X POST -d "password=<your_password>&username=<your_username>&email=<your_email>" https://messaging-django.herokuapp.com/api/users/registration
##### If all data is valid, respond will be:
> {
>   "email": "your_email",
>   "username": "your_username",
>   "token": "your_token"
> }
#### Logging In
> curl -X POST -d "password=<your_password>&username=<your_email>" https://messaging-django.herokuapp.com/api/users/registration
* Notice that in username you should pass your Email!
##### Respond if Valid:
> { "token" : "your_token" }

### Except Registration & Login ALL endpoints require Authorization header
- "Authorization" : "Token <your_token>"
## Messages API
--- 
#### Sending Message:
> curl -X POST -d "sender=<your_username>&receiver=<user_you_would_like_to_send_to>&message=<your_message>&subject=<your_subject>&unread=True"  https://messaging-django.herokuapp.com/api/messages/
##### If valid response from server:
> { "detail" : "created successfully" }
#### Deleting Message:
> curl -X POST https://messaging-django.herokuapp.com/api/messages/<message_id>/
#### Reading Message:
> curl -X POST -d https://messaging-django.herokuapp.com/api/messages/<message_id>/
#### All received Massages:
> curl GET https://messaging-django.herokuapp.com/api/users/<your_username>/received_messages/
#### All sent Massages:
> curl GET https://messaging-django.herokuapp.com/api/users/<your_username>/sent_messages/
#### All received **UNREAD** Massages:
> curl GET https://messaging-django.herokuapp.com/api/users/<your_username>/received_unread_messages/

## Installation locally:
1. git clone https://github.com/BenK93/MessagingAPI.git
2. pipenv install -r requirements.txt
3. pipenv shell
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver 
   
* will be available on `http://localhost:8000`


