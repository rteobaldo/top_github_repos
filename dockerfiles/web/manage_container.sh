#!/bin/bash
export DATABASE_URL=$DATABASE_PREFIX://$POSTGRES_USER:$POSTGRES_PASSWORD@postgres:5432/$POSTGRES_DB

exec python /app/manage.py $@
