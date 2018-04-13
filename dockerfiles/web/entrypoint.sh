#!/bin/bash
set -e
cmd="$@"

export DATABASE_URL=$DATABASE_PREFIX://$POSTGRES_USER:$POSTGRES_PASSWORD@postgres:5432/$POSTGRES_DB

function postgres_ready(){
python << END
import sys
import psycopg2
import environ
import dj_database_url

env = environ.Env()
DATABASE_URL = env('DATABASE_URL')
db_settings = dj_database_url.parse(DATABASE_URL)

try:
    conn = psycopg2.connect(
        database=db_settings['NAME'],
        user=db_settings['USER'],
        password=db_settings['PASSWORD'],
        host=db_settings['HOST'],
        port=db_settings['PORT']
    )

except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

function check_default_superuser(){
python << END
import os
import django
import environ

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
env = environ.Env()

if env('SUPERUSER_USERNAME') and env('SUPERUSER_PASSWORD'):
    from django.contrib.auth.models import User

    if not User.objects.filter(username=env('SUPERUSER_USERNAME')).exists():
        user = User(username=env('SUPERUSER_USERNAME'))
        user.set_password(env('SUPERUSER_PASSWORD'))
        user.is_superuser = True
        user.is_staff = True
        user.save()
    else:
        print("Already have an superuser")
else:
    print("Superuser settings not defined, passing...")
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - waiting"
  sleep 1
done

echo "Migrating database"
python /app/manage.py migrate

echo "Collecting static"
python /app/manage.py collectstatic --noinput

echo "Checking for default superuser"
check_default_superuser;

# echo "Executing tests"
# python /app/manage.py test core

exec $cmd
