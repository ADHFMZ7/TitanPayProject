# Titan Payment Platform

This web app allows users to sort, pay, and store their payment information.

It uses the Flask we microframework.

To run the app in a local server, install the requirements and run `./python3 run.py`

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
- `id`
- `date`
- `card`
- `amount`
- `cycle`
- `paid`
- `user_id`

- `__repr__()`: returns a string that represents purchase data

### Other Functions
-`create_user(request)`: This function takes in an http request uses it to build a user and add it to the database.
-`create_purchase(request)`: This function takes in an http request uses it to build a purchase and add it to the database.

## Views

-`load_user(id)`: This function takes an id and returns the respective `User` instance.
-`login()`: This functions authenticates users and redirects the user to the proper page.
-`signup()`: This function allows the users to create a new account and then redirects the user to the login page.
-`transaction()`: This function lets users add a new transaction to their account.
-`home()`: This function makes sure the user is authenticated and takes them to their homepage.
-`logout()`: This function logs out the user and sends them back to the login page.
-`info()`: This function makes sure the user is authenticated and takes them to a page to view their account information


## Javascript

Some javascript is also used in other parts of the program.

- `sortBy(column)`: This function takes in a column number of an html table as input, and sorts it by the values in that column.

