# Titan Payment Platform

This web app allows users to sort, pay, and store their payment information.

It uses the Flask we microframework 

To run the app, install the requirements and run `./python3 run.py`

## Database

The application uses the sqlite3 database model to store the information.

It does this in two tables:

### Users

- `id`
- `username`
- `pword`
- `name`
- `phone`
- `country`
- `address`
- `purchases`

 - `get_id()`: returns id of user
 - `calculate_balance()`: calculates current balance of user
 - `__repr__()`: returns a string that represents current user 


### Purchases
 -`id`
 -`date`
 -`card`
 -`amount`
 -`cycle`
 -`paid`
 -`user_id`

 -`__repr__()`: returns a string that represents purchase data

### Other Functions


##