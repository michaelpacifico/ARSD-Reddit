# Reddit Recovery Dashboard

All: These instructions could be more clear... wherever you run into setup issues or questions, please make notes for documentation purposes.

Use this video to set up postgres. https://www.youtube.com/watch?v=7EeAZx78P2U

In Postgres terminal/GUI: The URI and credentials need to be the same!

EITHER:
- set postgres user password to admin
- create database "first"
- create table (CREATE TABLE users(id SERIAL PRIMARY KEY,username VARCHAR(25) UNIQUE NOT NULL);)

OR:
Change this line in init_py:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/first'
to
'postgressql://[username]:[password]@localhost/[databasename]'

These are the commands to run from a python terminal.

03/30/2022 Update: to set up new db models:
- delete old table(s) using psql (drop table users;)
- run createTables.sql or copy and paste the code
- run the code below in vscode terminal (or however you did it before)

```
python
from dashboard import db
db.create_all()
```

01/24/2023 Update: to start the dashboard from Python terminal (running in "ARSD-Reddit" directory)

```
from dashboard import __init__
from dashboard import app
app.run(debug=False)
```

Is it running?
Open a web browser to: http://127.0.0.1:5000/
Go to "Link Account" (note: this should probably be called "Sign In") 
