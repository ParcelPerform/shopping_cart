#!/bin/bash

until psql -h "$PGHOST" -U "postgres" -d "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done


# Connect DB
psql -h $PGHOST -U postgres -d postgres -w --command "CREATE USER $PGUSER WITH SUPERUSER PASSWORD '$PGPASSWORD';"
psql -h $PGHOST -U postgres -d postgres -w --command "ALTER USER $PGUSER CREATEDB;"
psql -h $PGHOST -U postgres -d postgres -w --command "CREATE DATABASE $PGDATABASE OWNER=$PGUSER;"

# start web service
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
