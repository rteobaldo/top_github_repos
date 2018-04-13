#!/bin/bash

# stop on errors
set -e

# we might run into trouble when using the default `postgres` user, e.g. when dropping the postgres
# database in restore.sh. Check that something else is used here
if [ "$POSTGRES_USER" == "postgres" ]
then
    echo "Restoring as the postgres user is not supported, make sure to set the POSTGRES_USER environment variable"
    exit 1
fi

# export the postgres password so that subsequent commands don't ask for it
export PGPASSWORD=$POSTGRES_PASSWORD

# check that we have an argument for a filename candidate
if [[ $# -eq 0 ]] ; then
    echo 'Usage:'
    echo '    docker-compose run postgres restore <backup-file>'
    echo ''
    echo 'To get a list of available backups, run:'
    echo '    docker-compose run postgres list-backups'
    exit 1
fi

# set the backupfile variable
BACKUPFILE=/backups/$1

# check that the file exists
if ! [ -f $BACKUPFILE ]; then
    echo "Backup file not found"
    echo 'To get a list of available backups, run:'
    echo '    docker-compose run postgres list-backups'
    exit 1
fi

echo "Un-tar backup file"
echo $BACKUPFILE
echo ${BACKUPFILE::-4}
tar -xvf $BACKUPFILE

echo "Beginning restore from $1"
echo "-------------------------"

# restore the database
echo "Restoring database $POSTGRES_DB..."
psql -h localhost -U $POSTGRES_USER < ${BACKUPFILE::-4}

# remove temporary extracted file
rm ${BACKUPFILE::-4}
