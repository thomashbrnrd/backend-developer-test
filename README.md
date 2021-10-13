# Backend Developer Test

### Subject
Please find the original readme here : https://github.com/SORTEDfood/backend-developer-test

### Requirements
- `docker`
- `docker compose`

### About docker compose

We are using here the command `docker compose` which is a replacement for the `docker-compose` command.

##### MacOs & Windows

Docker compose (v2) should come already packed up with docker

##### Linux

https://docs.docker.com/compose/cli-command/#install-on-linux

### Useful commands

##### Get in the right directory
`cd backend_test`

##### Run the stack
`make`

##### Run the migrations
`make migrate` (the stack need to run)

##### Run the tests
`make test`  (the stack need to run)

##### Bash into the main container
`make bash` (the stack need to run)

### Main routes

- http://localhost:8000/api/
- http://localhost:8000/swagger/
- http://localhost:8000/admin/

### Notes

- If you want to use the Django Admin, you will need to create a superuser.
  - `make bash`
  - `python manage.py createsuperuser`
- From my understanding of the subject, it was not 100% clear of how to handle the user for initials `ShoppingLists`(provided by the subject in the `data` directory). I took the decision to create one `User` per `ShoppingList`. These users are filled with fake data from the `Faker` library.
- The API has some throttling : **60 requests per minute**.
