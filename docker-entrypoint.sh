#!/bin/sh
set -e

cd /project

# Execute database migrations
python manage.py migrate

exec "$@"
    