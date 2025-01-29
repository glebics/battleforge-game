#!/bin/sh

echo "Waiting for PostgreSQL to start..."
until pg_isready -h db -p 5432 -U ${POSTGRES_USER}; do
  sleep 1
done

echo "PostgreSQL started"

exec "$@"
