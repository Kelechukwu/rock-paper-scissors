# rock-paper-scissors
Simple API for Rock Paper & Scissors using Django Rest Framework

## Getting started
1. Install docker and Docker-compose for easy setup. 

2. Run `docker-compose build && docker-compose up -d`.

3. You should be able to access the API on port `localhost:8000`

4. Stop the containers by running `docker-compose down`

## Tests
Pytest is the testing suite for this application. Test can be found in the  `tests/` folder of individual django apps. For example in `games/tests`

To run all tests execute this command while containers are still active
```docker exec -it RPS-server pytest```

Integration tests are split into 
1. *Validations* : custom validation logic that throws errors when the state of the system is not ideal for a request to be successful
2. *Endpoints* : happy path to test how ths system should behave when all is okay.


## Database 
Postgres SQL database is used in this application via docker-compose. Migrations
run automatically when the docker-compose "build and up " commands are executed

The DB schema definition can be seen in `games/models.py`


## Basic API call flow

1) Create a new game
```
POST /game HTTP/1.1
Content-Type: application/json

{
    "game_id": 1,
    "is_computer_opponent": true,
}
```
2) Players join the new game
```
POST /game/1/join HTTP/1.1
Content-Type: application/json

{
    "name": "John Lennon",
}
```
3) Game is started
```
PATCH /game/1 HTTP/1.1
Content-Type: application/json

{
    "status": "STARTED",
}
```
4) Players take turns to play the game 
```
PATCH /game/1/play HTTP/1.1
Content-Type: application/json

{
    "player_id": 1,
    "hand": SCISSORS
}
```