#!/bin/bash

# Connect DB
psql -h $PGHOST -U postgres -d postgres -w --command "CREATE USER $PGUSER WITH SUPERUSER PASSWORD '$PGPASSWORD';"
psql -h $PGHOST -U postgres -d postgres -w --command "ALTER USER $PGUSER CREATEDB;"
psql -h $PGHOST -U postgres -d postgres -w --command "CREATE DATABASE $PGDATABASE OWNER=$PGUSER;"

# start web service
python3 manage.py runserver 0.0.0.0:8000
