database.py 
This file is that handles the connection, sessionlocal, and base. Connecting the engine to the database 

Models.py 
This file handles the database name and creation of colomns in the database with features, from primary_key, index, unique also connects to database file 

Schemas.py 
handles the class for Userbase, user create and user response, also handles the basemodel in what type datatype needed 

crud.py 
This file handles hasting, checking if the two of the same kind names for emails exist, build the db model, stage, write, refresh and return 

main.py
create the database session  and ensures it is closed after use also, routing, app and dependcy  