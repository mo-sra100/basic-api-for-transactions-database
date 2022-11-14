LEND DIRECT INTERVIEW 3RD STAGE

# Introduction

The task is to create a python RESTful API recieving and returning application/json content (using your choice of the Flask or FastAPI frameworks) that will similuate a small data update microservice 

A sqlite3 db has been provided, the table 'transactions' has been populated with some sample data, you can edit the db structure if you see fit.

This is a small sample of 85 rows but bear in mind this could be millions in production

Hint: Postman is very useful for API development

# Specification 

The API should have 4 routes :

## /add : 

saves data provided in the request body to the 'transactions' table

example request body: ```{'transaction_id' : 'E2D99999-9999-4C2D-E999-6B04A8C0422A', 'date' : '2022-04-27', 'price' : 100000, 'address' : '1 Copperbeech Close'}```

respond with status and message


## /update : 

update an existing row in the transactions table identified by transaction_id

example request body: ```{'transaction_id' : 'E2D99999-9999-4C2D-E999-6B04A8C0422A', 'date' : '2022-04-27', 'price' : 100000, 'address' : '1 Copperbeech Close'}```

fields not being updated will be present but with values set to null, no field should be updated to a null value

respond with status and message


## /delete : 

deletes a row identified by transaction_id

example request body: ```{'transaction_id' : 'E2D99999-9999-4C2D-E999-6B04A8C0422A'}```

respond with status and message


## /query : 

returns rows matching request criteria as json data

API should filter on any combination of min date, max date, min price, max price and address

example request body: ```{'max_date' : '2022-09-27', 'min_date' : '2022-04-27', 'max_price' : 100000, 'min_price' : 500, 'address' : '1 Copperbeech Close'}```

fields not being queried on will be present but with values set to null


# Submission 

Please submit your project directory as a .zip, containing a populated requirements.txt file 

API should be run via run.py

Additionally submit a paragraph or two detailing any design choices you have made, factors you considered and any issues you believe the solution would face scaling up
