#!/bin/bash
# stop on errors
set -e

# we might run into trouble when using the default `postgres` user, e.g. when dropping the postgres
# database in restore.sh. Check that something else is used here
if [ "$POSTGRES_USER" == "postgres" ]
then
    echo "creating a backup as the postgres user is not supported, make sure to set the POSTGRES_USER environment variable"
    exit 1
fi

# export the postgres password so that subsequent commands don't ask for it
export PGPASSWORD=$POSTGRES_PASSWORD

echo "creating backup"
echo "---------------"

FILENAME=bckp_$(date +'%Y%m%dT%H%M').sql
pg_dump -h localhost -U $POSTGRES_USER > /backups/$FILENAME

tar -zcvf "/backups/$FILENAME.tgz" backups/$FILENAME
rm /backups/$FILENAME

echo "successfully created backup $FILENAME"
